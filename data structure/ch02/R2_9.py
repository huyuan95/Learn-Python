class Vector:
    '''
    Represent a vector in a multidimensional space.
    '''
    def __init__(self, d):
        '''Create d - dimensional vector of zeros.'''
        if type(d) == int:
            self._coords = [0]*d
        elif type(d) == list:
            self._coords = [0] * len(d)
            for j in range(len(d)):
                if type(d) == int or type(d) == float:
                    self._coords[j] = d[j]
                else:
                    raise TypeError(
                    'Must be dimension of Vector or a number list for Vector')
        else:
            raise TypeError(
                'Must be dimension of Vector or a number list for Vector')
    
    def __len__(self):
        '''Return the dimension of the vector.'''
        return len(self._coords)
    
    def __getitem__(self, j):
        ''''Return jth coordinate of vector.'''
        return self._coords[j]
    
    def __setitem__(self, j, val):
        '''Set jth coordinate of vector to given value.'''
        self._coords[j] = val
                        
    def __add__(self, other):
        '''Return sum of two vectors.'''
        if len(self) != len(other):  # relies on len method
            raise ValueError("dimensions must agree")
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __sub__(self, other):
        '''Return substract of two vectors'''
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self)) #start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    
    def __neg__(self):
        '''Return negnative of vector'''
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result
    
    def __mul__(self, other):
        '''Return multiple result of vector to a scalar or a vector'''
        result = Vector(len(self))
        if type(other) == int or type(other) == float:
            for j in range(len(self)):
                result[j] = self[j] * other
        elif type(other) == Vector:
            for j in range(len(self)):
                result[j] = self[j] * other[j]
        else:
            raise TypeError("only multiply int, float or another Vector")
        return result
    
    def __rmul__(self, other):
        '''Return multiple result of vector to a scalar or a vector'''
        result = Vector(len(self))
        if type(other) == int or type(other) == float:
            for j in range(len(self)):
                result[j] = self[j] * other
        elif type(other) == Vector:
            for j in range(len(self)):
                result[j] = self[j] * other[j]
        else:
            raise TypeError("only multiply int, float or another Vector")
        return result
    
    def __eq__(self, other):
        '''Return True if vector has same coordinates as other.'''
        return self._coords == other._coords
    
    def __ne__(self, other):
        '''Return True if vector differs from other.'''
        return not self == other  # rely on existing eq definition
    
    def __str__(self):
        '''Produce string representation of vector.'''
        return '<' + str(self._coords)[1:−1] + '>'  # adapt list representation
