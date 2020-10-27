# Author: Henry Newcomer
# Date: 2020-09-04

import random

# Questions 1 & 2

grade = 0 # Assume worse-case by default
passing = False # Assume false by default

# "Magic numbers" like 70 should typically be referenced as a variable, enum, etc.,
# not by the number itself
# It's generally bad-practice to have numbers randomly mixed into the logic like this
# from what I've read; consider referencing the numbers, instead.
#
# While the conditional formatting you're about to see isn't used much, it's sometimes
# a nice shortcut for testing simple conditions. This is Python's equivalent of a "ternary operator."
passing = True if (grade > 70) else False

# Questions 3 & 4

stringCorrectResult = "Congratulations, you guessed correctly!"
stringIncorrectResult = "Sorry, incorrect guess."

# Let's make this keep playing unless you quit (but keep it to one guess per game)
keepPlaying = True

# Keep playing as long as the variable "keepPlaying" is True (spoiler: it's always true this time)
while keepPlaying:
    # Use some psuedo-randomization to have the computer pick an int
    randomNum = random.randrange(1, 10)

    numGuessed = int(input("Choose a whole number between 1 and 10: "))

    if (numGuessed == randomNum):
        print(stringCorrectResult)
    elif (numGuessed < randomNum):
        # These else-ifs are where I'd probably use another ternary operator again, though.
        print("The correct answer was more than that.")
    elif (numGuessed > randomNum):
        print("The correct answer was less than that.")
    else:
        print(stringIncorrectResult)

    # Alright, let's see what the computer's number actually was
    print("\tThe AI picked: " + str(randomNum))

    # IMPORTANT thing to notice! There's nothing telling keepPlaying to ever stop.
    # This is called an "infinite loop," since it never has an instance that terminates the loop.
    # In the real world, you might attach buttons such as "Close" or commands like "exit" to
    # respond by setting keepPlaying to false, which would finally finish this loop (thereby
    # ending the game)
