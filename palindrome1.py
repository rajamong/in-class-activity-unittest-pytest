# creates a class called palindrome1
class palindrome1:
    # creates an empty constructor
    def __init__(self):
        pass

    # combines the first name and last name
    def palidromecheck(self, input):
        for x in range(0, int(len(input)/2)):
            if input[x] == input[len(input) - x - 1]:
                return True
            else:
                return False