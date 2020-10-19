
# Author: Henry Newcomer

# A common phrase you'll hear in programming is "Don't Repeat Yourself."
# Since the section headers appear in each section with the only difference
# being which letter is used, we can just make it into something reusable.
def showHeader(sectionLetter):
    return "\n==== Section " + sectionLetter + " ===="

def sectionA():
    # Since we're starting lists soon, here's an example
    # Think of them as just a *container* (similar to an "array" in other
    # programming languages) of *things* (called "elements").
    me = ["Henry", "Newcomer"]
    index = 0
    print(showHeader("A"))
    while index < 3:
        # Without this increment, it'd be an infinite loop, which is
        # almost always not something we'd want (unwanted infinite loops cause
        # hang-ups/crashes since they never terminate).
        index += 1
        # Taking what the assignment's sentence says too literally...
        print("a spec- " + me[0] + " "+ me[1] + " -ific phrase.")

def sectionB():
    # I make this variable global so that the sectionC() function can share it
    global timesToLoop
    timesToLoop = input("# of loops: ")
    index = 0 # Now I'm starting to repeat myself. This would be a good time
              # to think about what similarities and differences sectionA and
              # sectionB do (and C, later on). For example, this could be
              # rewritten into a single function instead of three, just like
              # what showHeader() does (which itself could then be moved/removed
              # into the function too).
              # Remember: it's less work, easier to maintain, and easier to
              # understand/interpret what's going on, if you're able to group
              # things together.
    print(showHeader("B"))
    print("Printing my major " + str(timesToLoop) + " times\n--------------------------------")
    while index < int(timesToLoop):
        index += 1
        print("Major: _________ (Line #" + str(index) + ")")

def sectionC():
    global timesToLoop
    index = 0
    totalMultiplied = 1
    print("timesToLoop: "+timesToLoop)
    print(showHeader("C"))
    while index < int(timesToLoop):
        index += 1
        totalMultiplied *= int(input("Enter a number to use to multiply: "))
    print("Final total: " + str(totalMultiplied))

# Groups the functions together in the order I want them to process.
def runSections():
    sectionA()
    sectionB()
    sectionC()

# Now that everything's organized, start its execution.
runSections()
