# imports pytest functionality
import pytest
# imports palindrome class from palindrome program
import palindrome2


def test1():
    input = "racecar"
    assert palindrome2.palidromecheck(input) == True

def test2():
    input = "gretel"
    assert palindrome2.palidromecheck(input) == False

def test3():
    input = "peep"
    assert palindrome2.palidromecheck(input) == True


if __name__ == "__main__":
    pytest.main()