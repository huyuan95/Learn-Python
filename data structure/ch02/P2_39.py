from abc import ABCMeta, abstractmethod

class Polygon:
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def __init__(self, points):
        self._points = points
    

class Triangle(Polygon):
    
    def __init(self, points):
        if len(points) != 3:
            raise ValueError('Need 3 points')
        super().__init__(points)
    
    def get_area(self):
        sum = 0.0
        for i in (range(3)-1):
            sum += (self._points[i][0] * self._points[i+1][1] - self.points[
                i+1][0] * self._points[i][1])
        sum += (self.points[2][0]*self._points[0][1] - self._points[0][
            0]*self._points[2][1])
        return sum/2
    
    def get_perimeter(self):
        perimeter = 0
        for i in (range(3) - 1):
            perimeter += sqrt((self._points[i+1][0]-self._points[i][0])**2+
                              (self._points[i + 1][1] - self._points[i][
                                  1]) ** 2)
        perimeter += sqrt((self._point[2][0]-self._points[0][0])**2+\
                     (self._point[2][1]-self._points[0][1])**2)
        return perimeter
