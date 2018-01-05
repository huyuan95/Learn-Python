import unittest

from city_functions import city_country

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        city_country_name=city_country('santiago','chile')
        self.assertEqual(city_country_name, 'Santiago, Chile')

    def test_city_country_population(self):
        ccp=city_country('santiago', 'chile', population = 5000000)
        self.assertEqual(ccp, 'Santiago, Chile - population 5000000')

unittest.main()
