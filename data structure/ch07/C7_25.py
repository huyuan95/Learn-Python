class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        self._tail = None
        self._header = self._Node(None, None)
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        else:
            return self._header._next._element
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        else:
            answer = self._header._next._element
            self._header._next = self._header._next._next
            self._size -= 1
            if self.is_empty():
                self._tail = None
            return answer
    
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._header._next = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        
