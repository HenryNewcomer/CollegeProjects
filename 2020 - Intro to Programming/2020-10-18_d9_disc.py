# Author: Henry Newcomer

countries = ["Mexico", "Canada", "USA", "Germany"]
print("Third element: ", countries[2])
countries[3] = "France"
print("  -------------\nList of countries:")
for country in countries:
    # The weird "u" tells Python to show a unicode-escaped character.
    # Since it's a specific character and not an actual "string," note
    # the single-quotes being used.
    print("\t", u'\u047B', country)

#######################
# Start of question 5
#######################

print("  -------------\n")
friends = ["A.A. Ron",
           "DeNice",
           "JayQuellin",
           "Belakeh",
           "Obama-sholama-niqua",
           "Dan Smith"]
checkFriend = input("Search for name: ")
friendFound = False
for name in friends:
    if checkFriend == name:
        friendFound = True
        break;
if friendFound:
    # This uses an "f-string" (requires Python 3.6 or higher)
    # See how I don't have to put +s everywhere, and can directly
    # reference the variable checkFriend?
    print(f"Yes, {checkFriend} is my friend.")
else:
    print("Sorry: Not in my friend's list.")

print("\n  -------------\nRandom numbers:")

randomNumbers = [8, 6, 7, 5, 3] #, 0, nii-iiii-iiine
for i in randomNumbers:
    output = "\t" + str(i) + " * 2 = " + str(i * 2)
    print(output)
