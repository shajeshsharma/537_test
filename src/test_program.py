import unittest
from program import add, divide

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2),3)

    # def test_bad_add(self):
    #     self.assertEqual(add(1,2),2)

    def test_divide(self):
        self.assertEqual(divide(4,2),2)

    def test_bad_divide(self):
        self.assertRaises(ZeroDivisionError)
        divide(4,2)    

if __name__ == '__main__':
    unittest.main()        
