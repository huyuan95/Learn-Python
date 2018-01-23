class Polynomial:
    def __init__(self, a):
        self._a = a
    
    def firstDev(self):
        result = []
        for i in range(len(self._a)):
            result.append(self._a[i]*(len(self._a)-i-1))
        return result
