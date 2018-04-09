from tree import Tree

class LinkedTree(Tree):
    class _Node:
        __slots__ = '_element', '_parent', '_children'
        def __init__(self, element, parent = None, children = []):
            self._element = element
            self._parent = parent
            self._children = children
        
    class Position(Tree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node
        
        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
    
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:  # convention for deprecated node
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None
    
    def __init__(self):
        self._root = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def root(self):
        return self._make_position(self._root)
    
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def num_children(self, p):
        node = self._validate(p)
        return len(node._children)
    
    def children(self, p):
        node = self._validate(p)
        return node._children
    
    def _add_root(self, e):
        if self._root is not None:
            raise ValueError
        self._size += 1
        self._root = self._Node(e)
        return self._make_position(self._root)
    
    def _add_children(self, p, e):
        node = self._validate(p)
        node._children.append(self._Node(e, node))
        self._size += 1
        return self._make_position(node)
    
    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
    
    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) > 1:
            raise ValueError('p has more than one children')
        child = node._children[0]
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            i = parent._children.index(node)
            parent._children[i] = child
        self._size -= 1
        node._parent = node
        return node._element
