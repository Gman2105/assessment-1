import unittest

from optimal_change import optimal_change

# add tests to cover different edge cases

class optimal_changeTestCase(unittest.TestCase):
    """Tests for optimal_change.py"""
    
    # check the math and the str 
    def test_1(self):
        self.assertTrue(optimal_change(46.57, 100), 'The optimal change for this item is 46.57 with an amount paid of $100 is 1 $50 bill, 3 $1 bills,1 $0.25 cent,1 $0.1 cent,1 $0.05 cent , 2 $0.01 cents.')
        
    def test_2(self):
        self.assertEqual(type(optimal_change(3, 4)), str)
    
    # check the function to see if you have enough money. 
    def test_3(self):
        self.assertTrue(optimal_change(200, 100), 'Not Enough Money')
        
    def test_4(self):
        self.assertEqual(type(optimal_change(2, 5)), str)
    
    #  check the function to see if you get change.
    def test_5(self):
        self.assertTrue(optimal_change(100, 100) == 'No Change')
        
if __name__ == '__main__':
    unittest.main() 