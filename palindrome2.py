# creates the palindrome checker function
def palidromecheck(input):
    for x in range(0, int(len(input)/2)):
        if input[x] == input[len(input) - x - 1]:
            return True
        else:
            return False
 
