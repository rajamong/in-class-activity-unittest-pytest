# creates the word counter function
def countwords(input):
    # removes spaced from the string input
    spacing = input.strip()
    count = 0

    for i in spacing:
        # increases count variable after every space
        if i == " ":
            count = count + 1

    # increase count by one because of last word not included
    count = count + 1  
    return count