import math


## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    try:
        if type(filename) == str:
            infile = open(filename, "r")
            print("File opened.")
        else:
            raise TypeError

    except FileNotFoundError:
        print("File open error")

    except TypeError:
        print("Filename should only be of string type!")

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    try:
        return num1 / num2

    except(TypeError):
        print("Type Error! Please enter an integer.")


## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    try:
        dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
        dist = math.sqrt(dist)

        return dist

    except(TypeError):
        print("Type Error! Please enter an integer.")


## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    try:
        test = temp[::-1]

        if(test == temp):
            return True

        else:
            return False

    except TypeError:
        print("Type Error! Please enter a string.")

# Value error when string passed in
## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))

        div = num1 / num2

        print("Your numbers divided is:", div)
    except:
        print("Please input numbers only")

## returns the squareroot of a particular number
def sq(num):
    try:
        return math.sqrt(num)

    except TypeError:
        print("Type Error! Please enter an integer")

    except ValueError:
        print("Please only input positive numbers!")


## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    try:
        if (type(first) == str) & (type(middle) == str) & (type(last) == str):
            print("Hello!")
            print("Welcome to the program", first, middle, last)
            print("Glad to have you!")
        else:
            raise TypeError

    except TypeError:
        print("Error: Only strings are allowed")


## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    try:
        print("Your item at", index, "index is", numbers[index])        
    except:
        print("Please put the right inputs")
    
