class SparseArray:
    class _Node:
        def __init__(self, e, index, next, prev):
            self._element = e
            self._index = index
            self._next = next
            self._prev = prev
        
    def __init__(self, A):
        self._header = _Node(None, -1, None, None)
        self._trailer = _Node(None, 0, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = len(A)
        for i in range(self._size):
            if A[i] != 0:
                j = i
                pre = self._insert_between(A[i], i, self._header,
                                           self._trailer)
        if self._trailer._index != 0:
            for i in range(j + 1: range(len())):
                if A[i] != 0
                    self._insert_between(A[i], i, self._trailer._prev,
                                         self._trailer)
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, e, index, predecessor, successor):
        newest = _Node(e, index, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        self._trailer._index += 1
        return newest
    
    def _setvalue(self, pos, e):
        if e != 0:
            pos._element = e
        else:
            pos._prev._next = pos._next
            pos._next._prev = pos._prev
            self._trailer._index -= 1
            pos._prev = None
            pos._next = None
            pos._element = None
    
    def __getitem__(self, j):
        if j >= self._size or j < 0:
            raise IndexError('index out of range')
        pos = self._header
        while pos._next._index <= j and pos._next is not self._trailer:
            pos = pos._next
            if pos._index == j:
                return pos._element
        return 0
    
    def __setitem__(self, j, e):
        if j >= self._size or j < 0:
            raise IndexError('index out of range')
        if e == 0:
            self._trailer._index += 1
            return None
        pos = self._header
        while pos._next._index <= j and pos._next is not self._trailer:
            pos = pos._next
            if pos.index == j:
                self._setvalue(pos, e)
        self._insert_between(e, j, pos._prev, pos)
