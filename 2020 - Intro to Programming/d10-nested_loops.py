# Author: Henry Newcomer
# Date: 2020-10-22

tableNumbers = [[2, 5, -6,  7],
                [8, 6,  9,  3],
                [1, 4,  3, -8]]

# Most programming languages would freak out about this list because
# of the mixed typed (strings and ints). Nope: not Python. :)
tableEmployees = [["Name",  "Age", "$alary/hr"],
                  ["John",  23,    17.00],
                  ["Bryan", 19,    12.50],
                  ["Rose",  31,    22.13]]

tableOutput = ""
tableNumberSum = 0
# This lets us loop through both tables within the same loop-code.
# It's just an extra nested loop
for table in tableNumbers, tableEmployees:
    for row in table:
        for element in row:
            # Since we're already using nested loops to iterate through the
            # table, we can just do Question #5 here, instead of duplicating
            # code, execution time, processing power.
            if table == tableNumbers:
                tableNumberSum += int(element)
            # This uses str.format to trim/format the output so it doesn't push
            # the vertical pipes out of alignment.
            tableOutput += "\t | {0: <5}".format(str(element))
        tableOutput += "\t|\n" # Adds a blank line after each row
    tableOutput += "\n" # Adds an extra blank line between different tables.

print(tableOutput)
print("Table Numbers sum:", tableNumberSum) # Question 5

#################
# Question 6
#################

print("\n")

def weeklySalary():
    personFound = False
    who = input("Whose weekly salary should we check?\n")
    for row in tableEmployees:
        # Was the entered input an actual name?
        if who in row:
            ###############
            # This looks confusing, but it's not.
            ###############
            # The first part (before the % symbol) is a string format. In this case,
            # it shows a float with two decimal places - just like money. *gasp*
            # That was thanks to a post on:
            # https://stackoverflow.com/questions/6149006/display-a-float-with-two-decimal-places-in-python
            # The second section (after the %), is just the $/hr-to-$/week conversion.
            # The "magic number" (google it) 40 is the amount of hours worked.
            weeklyResult = '%.2f' % (row[2] * 40)
            personFound = True
            print(f"Weekly salary for {who}: {weeklyResult}")
            break;
    if personFound == False:
        print(f"\"{who}\" not found.")

weeklySalary()
