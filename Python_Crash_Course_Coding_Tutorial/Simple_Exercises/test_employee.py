import unittest
from employee import Employee as e

class TestEmployee(unittest.TestCase):
    ''' Testing employee class'''

    def setUp(self):
        ''' Creating intial instances'''

        self.f_name = 'Bob'
        self.l_name = 'Belcher'
        self.salary = 35_000
        self.myraise = 2_500
        self.response1 = "The employee: 'Bob Belcher' had an annual salary of 35000 and a recent raise of 5000"
        self.response2 = "The employee: 'Bob Belcher' had an annual salary of 35000 and a recent raise of 2500"
        
    def test_give_default_raise(self):

        test1 = e(self.f_name,self.l_name,self.salary).give_raise()
        self.assertEqual(test1 , self.response1)


    def test_custom_raise(self):
        test2 = e(self.f_name, self.l_name, self.salary,self.myraise).give_raise()
        self.assertEqual(test2, self.response2)


if __name__ == '__main__':
    unittest.main()