import numpy as np
###
# Program that takes user input to create an array of any dimensions,
# and return the indexes of integers that are divisible by 2.
# The arrays created are also stored in a cache, allowing the user to view previously created arrays
###

###
# Things I want to modify:
#   - Finish 'menu', allowing the user to move freely between creating and viewing
#   - Clean up code; create functions for easily reusable code
#   - Find faster solutions to some of the numerous 'if' statements
###

# Creates 1D array from list provided by user
def create1DArray(list):
    arr = np.array([list])
    print("Here is the 1D array created:\n", arr)
    return arr


# Creates 2D array from list provided by user and reshapes it to be 2 dimensional
def create2DArray(list):
    arr = np.array([list])
    newArr = arr.reshape(2,3)
    print("Here is the 2D array created:\n", newArr)
    return newArr


# Creates 3D array from list provided by user and reshapes it to be 3 dimensional
def create3DArray(list):
    arr = np.array([list])
    newArr = arr.reshape(2,3,2)
    print("Here is the 3D array created:\n", newArr)
    return newArr


# Iterates through the array created and checks if each value is divisble by 2. If it is, then it returns
# a list containing the index at which the value is located
def diviByTwo(arr):
    indexList = []
    for index,value in np.ndenumerate(arr):
        if value%2 == 0:
            indexList.append(index)
    return indexList


# Main function to take in user input for integers in array and dimensions of array
def main():
    numDim = input("How many dimensions? ('Q' to quit): ")
    cache = []
    # While loop to keep creating user-made arrays until user enters sentinel value of 'Q'
    while numDim.upper() != "Q":
        listForArr = []
        numDim = int(numDim)
        if numDim == 1:
            numsInArr = int(input("How many integers in your 1D array?: "))
            for i in range(0,numsInArr):
                intsArr = int(input("Enter integers for array: "))
                listForArr.append(intsArr)
            arr = create1DArray(listForArr)
        if numDim == 2:
            for i in range(0,6):
                intsArr = int(input("Enter integers for array: "))
                listForArr.append(intsArr)
            arr = create2DArray(listForArr)
        if numDim == 3:
            for i in range(0,12):
                intsArr = int(input("Enter integers for array: "))
                listForArr.append(intsArr)
            arr = create3DArray(listForArr)
        
        cache.append(arr)
        indexList = diviByTwo(arr)
        print("Here are the positions of integers in the array that are divisible by 2:\n", indexList)
        # Give the user an option to create another array, view a previously created array, or quit the program
        repeatProgram = input("Create another array ('create'), view previous arrays ('view'), or quit program ('quit'): ")
        if repeatProgram.lower() == "create":
            numDim = input("How many dimensions? ('Q' to quit): ")
        if repeatProgram.lower() == "view":
            cacheValue = input("Which previous array would you like to view? (You have created %d): " % (len(cache)))
            # While loop that allows the user to view multiple previously created arrays until sentinel value of 'Q' is entered
            while cacheValue.upper() != "Q":
                cacheValue = int(cacheValue)
                print("Here is array number", cacheValue, ":\n", cache[(cacheValue-1)])
                cacheValue = input("View another previous array ('view') or quit ('Q')?: ")
                if cacheValue == "view":
                    cacheValue = input("Which previous array would you like to view?: ")
            break
        if repeatProgram.lower() == "quit":
            break
    

main()
    


