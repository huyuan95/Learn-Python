''' a class for restaurant'''

class Restaurant():
    def __init__(self, r_name, r_type, r_number=0):
        self.restaurant_name=r_name
        self.restaurant_type=r_type
        self.number_served=r_number

    def describe_restaurant(self):
        print("The name of the restaurant is %s." % self.restaurant_name)
        print("The type of the restaurant is %s." % self.restaurant_type)

    def open_restaurant(self):
        print("The restaurant is opening.")

    def set_number_served(self,number):
        self.number_served=number

    def increment_number_served(self,inc_number):
        if inc_number >= 0:
            self.number_served+=inc_number

if __name__ == "__main__":
    restaurant1=Restaurant("Papa John's","Pizza shop")
    restaurant2=Restaurant("Mcdonald's","diet")
    restaurant3=Restaurant("KFC","diet")

    restaurant1.describe_restaurant()
    restaurant1.increment_number_served(5)
    print('%d persons had eaten in the restaurant.' % restaurant1.number_served)
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()
