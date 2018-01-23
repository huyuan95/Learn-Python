import random

ANIMAL_SUM = 50

class Animal:
    def __init__(self, position, gender, strength):
        self._position = position
        self._gender = gender
        self._strength = strength
    
    def move(self, offset, move_flag):
        if move_flag == True:
            return self._postion
        else:
            if self._position + offset > ANIMAL_SUM - 1 or self._position + \
                    offset < 0:
                return self._postion
            else:
                self._position += offset
                return self._position + offset
    
    def get_position(self):
        return self._position
    

class Bear(Animal):
    def __init__(self, position, gender, strength):
        super().__init__(position, gender, strength)
        
    def move(self, offset, move_flag):
        if move_flag == True:
            return self._position
        elif self._position + offset > ANIMAL_SUM - 1 or self._position + \
                    offset < 0:
            return self._position
        else:
            if type(river[self._position + offset]) == Bear:
                if self._gender == river[self._position + offset]._gender:
                    river[self._position + offset] = Bear(self._position +
                        offset, self._gender, max(self._strength,
                        river[self._position + offset]._strength))
                else:
                    river[self._position + offset] = Bear(self._position +
                    offset, random.choice(['m', 'f']), (self._strength +
                    river[self._position + offset]._strength)/2)
                river[self._position] = None
            else:
                river[self._position + offset] = river[self._position]
                river[self._position] = None
                self._position += offset
                
    
class Fish(Animal):
    def __init__(self, position, gender, strength):
        super().__init__(position, gender, strength)
    
    def move(self, offset, move_flag):
        if move_flag == True:
            return self._position
        elif self._position + offset > ANIMAL_SUM - 1 or self._position + \
                    offset < 0:
            return self._position
        else:
            if type(river[self._position + offset]) == Fish:
                if self._gender == river[self._position + offset]._gender:
                    river[self._position + offset] = Fish(self._position +
                        offset, self._gender, max(self._strength,
                        river[self._position + offset]._strength))
                else:
                    river[self._position + offset] = Fish(self._position +
                    offset, random.choice(['m', 'f']), (self._strength +
                    river[self._position + offset]._strength)/2)
                river[self._position] = None
            elif type(river[self._position + offset]) == Bear:
                    return self.get_position
            else:
                river[self._position + offset] = river[self._position]
                river[self._position] = None
                self._position += offset
    
river = ['']*ANIMAL_SUM

for i in range(len(river)):
    river[i] = random.choice([Bear(i, random.choice(['m','f']), 1.0), Fish(i,
    random.choice(['m','f']), 0.5), None])

while True:
    for i in range(len(river)):
        if river[i] != None:
            river[i].move(random.choice([1, -1]), random.choice([True, False]))
    print(river)
#    input()
