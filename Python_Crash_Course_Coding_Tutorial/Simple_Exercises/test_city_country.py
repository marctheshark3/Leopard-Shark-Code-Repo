import unittest
from city_country import myhome

class CityTestCase(unittest.TestCase):
    ''' Test for 'city_country.py '''

    def test_myhome(self):
        ''' Does "Boston" and "USA" work?'''

        tested_myhome = myhome('Boston','USA')

        self.assertEqual(tested_myhome, 'Boston, Usa')
    def test_myhome_population(self):
        ''' Adding an additional test for the population case'''

        popu_myhome = myhome('Boston', 'USA', 3_900_000_000)
        self.assertEqual(popu_myhome, 'Boston, Usa, 3900000000')

if __name__ == '__main__':
    unittest.main()