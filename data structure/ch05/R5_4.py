import ctypes

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""
    
    def __init__(self):
        """Create an empty array"""
        self._n = 0       # count actual elements
        self._capacity = 1      # default array capacity
        self._A = self._make_array(self._capacity) # low_level array
        
    def __len__(self):
        """Return number of elements stored in the array"""
        return self._n
    
    def __getitem__(self, k):
        """Return element in index k"""
        if k < -self._n or k >= self._n:
            raise IndexError('invalid index')
        return self._A[k if k >= 0 else self._n + k]    # Retrieve from array
    
    def append(self, obj):
        """Add object to the end of the array"""
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1
    
    def _resize(self, c):    # non-public utility
        """Resize internal array to capacity c"""
        B = self._make_array(c)  # new(bigger) array
        for k in range(self._n): # for each existing value
            B[k] = self._A[k]
        self._A = B      # using the bigger array
        self._capacity = c
    
    def _make_array(self, c): # non-public utility
        """Return new array with capacity c"""
        return (c * ctypes.py_object)()
    
    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward"""
        if k < -self._n or k >= self._n:
            raise IndexError('invalid index')
        k = k if k >= 0 else self._n + k
        if self._n == self._capacity:  # not enough room
            B = self._make_array(2 * self._capacity)  # so double capacity
            self._capacity = 2 * self._capacity
            for j in range(0, k - 1):
                B[j] = self._A[j]
            B[k] = value
            for j in range(k, self._n):
                B[j+1] = self._A[j]
            self._A = B
        else:
            for j in range(self._n, k, -1):
                self._A[j] = self._A[j-1]
            self._A[k] = value
        self._n += 1
    
    def pop(self):
        if self._n - 1 < self._capacity / 4:
            self._resize(self._capacity / 2)
        self._n -= 1
