import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.myEmployee = Employee('Vincent', 'Hu', 50000)

    def test_give_default_raise(self):
        self.myEmployee.give_raise()
        self.assertEqual(55000, self.myEmployee.salary)

    def test_give_custom_raise(self):
        self.myEmployee.give_raise(3000.5)
        self.assertEqual(53000.5, self.myEmployee.salary)

unittest.main()
