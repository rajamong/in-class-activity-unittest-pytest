# imports unittest functionality
import unittest
# imports wordcount1 class from wordcount1 program
from wordcount1 import wordcount1

class testCase(unittest.TestCase):
    def setUp(self):
        self.wordcount = wordcount1()

    # tests the word counting functionality with a string input
    def test1(self):
        self.assertEqual(self.wordcount.countwords('hi my name is gretel'), (5))
    
    # tests the word counting functionality with a string input
    def test2(self):
        self.assertEqual(self.wordcount.countwords('hello'), (1))
    
    # tests the word counting functionality with a string input
    def test3(self):
        self.assertEqual(self.wordcount.countwords('i love software engineering'), (4))


if __name__ == "__main__":
    unittest.main()