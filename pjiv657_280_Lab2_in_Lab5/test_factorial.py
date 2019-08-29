import unittest
import maths

class FactorialTest(unittest.TestCase):
    def test_factorial(self):
        num = 3
        fact = maths.factorial(num)
        if fact == num * 2:
            pass
        else:
            self.fail('test failed')