import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do cities and countries like 'Santiago, Chile' work?"""
        pair = city_country('santiago', 'chile')
        self.assertEqual(pair, 'Santiago, Chile')

    #added new test
    def test_city_country_population(self):
        """Do cities, countries and population like 'Santiago, Chile - 5000000' work?"""
        pair = city_country('santiago', 'chile', '5000000')
        self.assertEqual(pair, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()