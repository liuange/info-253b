# Assignment Instructions:

#     Create a Python file titled "lab_1.py"
#     Define a function called "numToString" that accepts an integer as a parameter
#     This function should return the digit string.

# Please make sure you use the mentioned file name and the function name to ensure that all test cases pass!

# Submission Instructions:

#     You can upload your Python (lab_1.py) file to bCourses as a submission.
#     Each lab submission will be due Thursday at midnight before the next lab. Accordingly, this lab will be due before 11:59 pm next Thursday (February 2nd).

def numLookup(numString):
    '''
    Converts string integer to string digit name
    '''
    numMap = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
        }
    return numMap[numString]


def numToString(integer):
    '''
    Takes integer as input and returns a digit string.
    '''
    numString = str(integer)
    output = list(map(numLookup, numString))
    return " ".join(output)

# numToString(547)
