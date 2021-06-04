import unittest

from optimal_change import optimal_change

# add tests to cover different edge cases

class optimal_changeTestCase(unittest.TestCase):
    """Tests for optimal_change.py"""
    
    def test_1(self):
        self.assertEqual(optimal_change(99, 100), 1)
        
    def test_2(self):
        self.assertEqual(optimal_change(45, 100), 55)
    
    def test_3(self):
        self.assertNotEqual(optimal_change(99.99, 100), 0.01)
        
    def test_4(self):
        self.assertEqual(optimal_change(100, 100), 0)
    
    def test_5(self):
        self.assertTrue(optimal_change(100, 100) == 'No Change')
        
     # Your tests will go here
if __name__ == '__main__':
    unittest.main() 
