"""
Antonios Takos
Lab 8, unittest
Sep 29, 2025
Oct 6, 2025
"""
import unittest
import calculations
from employee import Employee # import class 'Employee' from 'employee.py'

# function to add and return the sum of two numbers
def addtwonumbers(a,b):
    return a+b

print("\n---- Example 1: test for equality -----")
# create a code to test function 'addtwonumbers'
class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addtwonumbers(2,3),5)

print("\n---- Example 2: unittest for calculations -----")
class TestCalculation(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(calculations.multiplythreenumbers(5),5)
        self.assertEqual(calculations.multiplythreenumbers(2,3),6)
        self.assertEqual(calculations.multiplythreenumbers(2,3,4),24)
        self.assertEqual(calculations.multiplythreenumbers(0),0)

    def test_division(self):
        self.assertEqual(calculations.dividetwonumbers(8,4),2)
        self.assertAlmostEqual(calculations.dividetwonumbers(9,2),4.5)
        self.assertEqual(calculations.dividetwonumbers(9,0),-1)
        self.assertIsNone(calculations.dividetwonumbers("a",2))

    def test_subtraction(self):
        self.assertEqual(calculations.subtracttwonumbers(5,2),3)
        self.assertEqual(calculations.subtracttwonumbers(4,5),-1)
        self.assertIsNone(calculations.subtracttwonumbers("u",7))
    
    def test_addition(self):
        self.assertEqual(calculations.addthreenumbers(5,2,4),11)
        self.assertEqual(calculations.addthreenumbers(7,2,3),12)
        self.assertIsNone(calculations.addthreenumbers(2, "b"))

print("\n---- Example 3: unittest for Employee -----")
class TestEmployee(unittest.TestCase):
    # create a test template
    def setUp(self):
        #create an instance of a new employee
        self.emp1 = Employee('Peter', 'Pan', 50000)

    # create a test for employee email
    def test_emailemployee(self):
        self.assertEqual(self.emp1.emailemployee, 'Peter.Pan@email.com')

        # create a test for employee full
    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, 'Peter Pan' )

        #update the first name
        self.emp1.first = "Will"

        #re-test full name
        self.assertEqual(self.emp1.fullname, 'Will Pan')

    # create a test for salary
    def test_salary(self):
        #test salary before the raise
        self.assertEqual(self.emp1.salary, 50000)

        # first, raise the salary first
        self.emp1.apply_raise()

        # second, test salary
        self.assertEqual(self.emp1.salary, 52500)



if __name__ =="__main__":
    unittest.main()