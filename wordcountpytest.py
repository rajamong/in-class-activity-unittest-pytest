# imports pytest functionality
import pytest
# imports palindrome class from palindrome program
import wordcount2


def test1():
    input = "hi my name is gretel"
    assert wordcount2.countwords(input) == 5

def test2():
    input = "hello"
    assert wordcount2.countwords(input) == 1

def test3():
    input = "i love software engineering"
    assert wordcount2.countwords(input) == 4


if __name__ == "__main__":
    pytest.main()