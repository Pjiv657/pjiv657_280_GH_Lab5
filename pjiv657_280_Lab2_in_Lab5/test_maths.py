import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        no1 = 1
        no2 = 3
        
        res = maths.add(no1, no2)
        
        if res == (no1 + no2):
            pass
        else:
            self.fail('test failed')
        pass # TODO

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        fib = maths.fibonacci(5)
        
        if fib == 5:
            pass
        else:
            self.fail('test failed')
        
        pass # TODO

    def test_convert_base_under10(self):
        num = 15
        n = 8
        
        conv_b = maths.convert_base(num, n)
        
        if conv_b == str(oct(num)[2:]):
            pass
        else:
            self.fail('Failed to convert')
            
        #print(conv_b)
                
        
    def test_convert_base_over10(self):
        num = 15
        n = 16
        
        conv_b = maths.convert_base(num, n)
        #Change result to suit question
        if conv_b == str(hex(num)[2:].upper()):
            pass
        else:
            self.fail('Failed to convert')
        #print(conv_b)
        
    def test_add_base(self):
        first = 2
        second = 6
        n = 2
        
        
        add = maths.add(first, second, n)
        
        if add == maths.convert_base(first+second, n):
            pass
        else:
            self.fail('test failed')
        
    def test_add_base_over10(self):
        first = 2
        second = 6
        n = 16
        
        
        add = maths.add(first, second, n)
        
        if add == maths.convert_base(first+second, n):
            pass
        else:
            self.fail('test failed')
        
        
        
# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
