
# @return new converted value
def convertTo(newType = None, degrees = 0):
    newValue = 0

    # Fahrenheit
    if newType == "f":
        # As a side-note, since Python allows variable types to change,
        # this is where you'd want to make sure we're dealing with actual
        # numbers from the 'degrees' argument. If it's not a number, the next
        # line could crash at runtime.

        # Assume we're coming from celsius
        newValue = round(((degrees * 9) / 5 ) + 32)
    # Celsius
    elif newType == "c":
        # Assume we're coming from fahrenheit
        newValue = round(((degrees - 32) / 9 ) * 5)
    else:
        print("Warning! No conversion type passed.")

    return newValue

# Change from 25 celsius to ?? fahrenheit
print("25 celsius is:", convertTo("f", 25), "fahrenheit")
# Change from 80 fahrenheit to ?? celsius
print("80 fahrenheit is:", convertTo("c", 80), "celsius")
