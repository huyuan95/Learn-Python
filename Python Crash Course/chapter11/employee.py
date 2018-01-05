class Employee():
    def __init__(self, f_name, l_name, sal):
        self.firstname = f_name
        self.last_name = l_name
        self.salary = float(sal)

    def give_raise(self, raise_salary = 5000):
        self.salary += raise_salary
