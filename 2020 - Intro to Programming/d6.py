# Author: Henry Newcomer
# Date: 2020-09-26

# Global variables like these are usually frowned on, just fyi
keepAsking = True
currentGrade = 0 # Assume the worst by default

def convertToLetter():
    # Python is weird; you have to declare that you're using a global
    # variable in different functions. Otherwise it makes its own local
    # variable named the same thing, but it doesn't update/effect the
    # actual global one.
    global keepAsking, currentGrade
    if currentGrade in range(90,100):
        print("A")
    elif currentGrade in range(80, 90):
        print("B")
    elif currentGrade in range(70, 80):
        print("C")
    elif currentGrade in range(60, 70):
        print("D")
    elif currentGrade in range(80):
        print("F")
    else:
        print("Invalid entry.")

def getInput():
    global keepAsking, currentGrade
    # Notice that I used single-quotes instead of double
    # That way I don't have to escape the double-quotes inside with \"
    # Also notice that I didn't wrap this input inside of an int()
    # That's because "q" wouldn't be an int
    enterGrade = input('Enter grade number (or "q" to quit): ')
    if str(enterGrade) == 'q':
        # This will stop the loop (essentially a "game loop")
        keepAsking = False
    else:
        currentGrade = enterGrade
        currentGrade = int(enterGrade)

# Keep asking until keepAsking becomes False
while keepAsking:
    getInput()
    convertToLetter()

print("Quitting...")
