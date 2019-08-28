import unittest
import logger

class LoggerTest(unittest.TestCase):
    def test_info(self):
        log = logger.Logger()
        log.info('Test logger info')
    
        
    def test_error(self):
        log = logger.Logger()
        log.error('Test logger error')

# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
