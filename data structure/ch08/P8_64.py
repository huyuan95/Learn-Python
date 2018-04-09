from binary_tree import BinaryTree
from dynamic_array import DynamicArray

class ArrayBinaryTree(BinaryTree, DynamicArray):
    
    class Position(BinaryTree.Position):
        
        def __init__(self, container, index):
            if index < 0:
                raise ValueError('Position index should not less than zero')
            self._container = container
            self._index = index
        
        def element(self):
            return self._container[self._index]
        
        def __eq__(self, other):
            return type(other) is type(self) and other._index == self._index
    
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._index < self._capacity:
            if self[p._index] is None:
                raise ValueError('p is no longer valid')
            else:
                return p._index
    
    def _make_position(self, index):
        return self.Position(self, index) if index < self._capacity - 1 and \
                index >= 0 else None
    
    def __init__(self):
        self._root = 0
        self._size = 0
        self._capacity = 0
        self._A = self._make_array(0)
        
    def __len__(self):
        return self._size
    
    def root(self):
        return self._make_position(self._root)
    
    def left(self, p):
        index = self._validate(p)
        return self._A[2 * index + 1]
    
    def right(self, p):
        index = self._validate(p)
        return self._A[2 * index + 2]
    
    def num_children(self, p):
        index = self._validate(p)
        count = 0
        if self.left(p) is not None:
            count += 1
        if self.right(p) is not None:
            count += 1
        return count
    
    def _add_root(self, e):
        if self.root is not None:
            raise ValueError('root exists')
        self._size = 1
        self[0] = e
        self._root = 0
        return self._make_position(self._root)
    
    def _add_left(self, p, e):
        index = self._validate(p)
        if self.left(p) == None:
            self._A[2 * index + 1] = e
            self._size += 1
            if self.capacity < 2*(2*index + 1) + 3:
                self._resize(2*(2*index + 1) + 3)
        else:
            self._A[2*index + 1] = e
        return self._make_position(2*index + 1)
    
    def add_right(self, p, e):
        index = self._validate(p)
        if self.right(p) == None:
            self._A[2 * index + 2] = e
            self._size += 1
            if self.capacity < 2 * (2 * index + 2) + 3:
                self._resize(2 * (2 * index + 2) + 3)
        else:
            self._A[2 * index + 2] = e
        return self._make_position(2 * index + 2)
    
    def _replace(self, p, e):
        index = self._validate(p)
        old = self._A[index]
        self._A[index] = e
        return old
    
