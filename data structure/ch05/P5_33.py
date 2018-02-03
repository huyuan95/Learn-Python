class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self._width = len(matrix)
        self._height = len(matrix[0])
    
    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
    
    def __add__(self, b):
        for i in range(self._width):
            for j in range(self._height):
                self.matrix[i][j] += b.matrix[i][j]
    
    def __mul__(self, b):
        if self._width != b.get_height():
            raise IndexError('invalid index')
        result = [[0] * b.get_width() for j in range(self._height)]
        for i in range(b.get_width()):
            for j in range(self._height):
                result[i][j] = sum(self.matrix[i][p] * b.matrix[p][j] for p
                                   in range(self._width))
        return Matrix(result)
