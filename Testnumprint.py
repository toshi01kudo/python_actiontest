import unittest
from numprint import numTest
 
class Testnumprint(unittest.TestCase):
    def test_numprint(self):
        val = "10"
        expect = "10"
        actual = numTest(numVal)
        self.assertEqual(expect, actual)
 
if __name__ == "__main__":
    unittest.main()