# imports unittest functionality
import unittest
# imports palindrome class from palindrome program
from palindrome1 import palindrome1

class testCase(unittest.TestCase):
    def setUp(self):
        self.palindrome = palindrome1()

    # tests the palindome checking functionality with a palindrome
    def test1(self):
        self.assertEqual(self.palindrome.palidromecheck('racecar'), (True))
    
    # tests the palindome checking functionality with a non-palindrome
    def test2(self):
        self.assertEqual(self.palindrome.palidromecheck('gretel'), (False))
    
    # tests the palindome checking functionality with a palindrome
    def test3(self):
        self.assertEqual(self.palindrome.palidromecheck('peep'), (True))


if __name__ == "__main__":
    unittest.main()