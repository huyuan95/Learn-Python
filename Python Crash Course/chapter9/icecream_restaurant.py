''' a class for incecream stand'''

import restaurant

class IceCreamStand(restaurant.Restaurant):
    def __init__(self, r_name, r_flavor, r_number=0):
        super().__init__(r_name, "Ice cream stand", r_number)
        self.flavors=r_flavor

    def stand_info(self):
        self.describe_restaurant()
        print('The flavor of the stand is:')
        for flavor in self.flavors:
            print(flavor)

if __name__ == "__main__":
    ice1=IceCreamStand("Jerry's",["vallina","Coco"])
    ice1.stand_info()
