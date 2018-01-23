class Flower:
    def __init__(self, name, number, price):
        self._name = name
        self._number = number
        self._price = price
    
    def get_name(self):
        return self._name
    
    def get_number(self):
        return self._number
    
    def get_price(self):
        return self._price
    
    def set_name(self, name):
        self._name = name
    
    def set_number(self, number):
        self._number = number
    
    def set_price(self, price):
        self._price = price

