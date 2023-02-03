import unittest
from test import support

def actual_func(a,b):
    return a+b

class MyTestCase1(unittest.TestCase):
    def test_feature_one(self):
        self.assertEqual(actual_func(1,2),3)
        self.assertEqual(actual_func(2, 2), 3)

if __name__ == '__main__':
    unittest.main()
