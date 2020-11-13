#
# Name: Henry Newcomer
# CSCI-130
#
#
# Program Description:
# Asks for items & prices, then calculates the total bill.

#######################
# Henry's edits (start)
#######################

def printHeading():
    output = "\
------------------------\n\
        Dinner for Two\n\
------------------------\n\
This program will ask for drink, entree and dessert\n\
for 2 different diners at a restaurant.\n\
You will be asked for a description and price for each item\n\
ordered, one customer at a time.\n\
After gathering customer details, the program will ask for\n\
(1) tax rate and (2) tip percentage.\n\
At the end, a dinner bill will be printed for both customers.\n"
    print(output)

def getTaxPercent():
    taxRate = float(input("Enter tax rate for this locale: "))
    if taxRate < 3:
        taxRate = 3
    elif taxRate > 8:
        taxRate = 8
    taxRateAdjusted = taxRate / 100
    return taxRateAdjusted

def getTipPercent():
    tipPercent = float(input("Enter tip percentage: "))
    if tipPercent < 10:
        tipPercent = 10
    elif tipPercent > 25:
        tipPercent = 25
    tipPercentAdjusted = tipPercent / 100
    return tipPercentAdjusted

# All this does is adds every number passed to it and returns the result
def addAll(*argv):
    n = 0
    for arg in argv:
        n += arg
    return n

def printBill(custNum, drinkItem, drinkPrice, entreeItem, entreePrice,
              dessertItem, dessertPrice, taxRate, tipPercent):
    initialTotal = addAll(drinkPrice, entreePrice, dessertPrice)
    tax = initialTotal * taxRate
    tip = initialTotal * tipPercent
    total = addAll(initialTotal, tax, tip)
    outputCustomerID = f"Customer #{custNum}"
    output = f"\
|*****************************|\n\
{'|' : <2}  {'Dinner Bill' : ^25} {'|' : <2}\n\
{'|' : <2}  {'-----------' : ^25} {'|' : <2}\n\
{'|' : <2}  {outputCustomerID : ^25} {'|' : <2}\n\
|*****************************|\n\
Drink: {drinkItem} $ {drinkPrice:.2f}\n\
Entree: {entreeItem} $ {entreePrice:.2f}\n\
Dessert: {dessertItem} $ {dessertPrice:.2f}\n\
Tax : $ {tax:.2f}\n\
Tip : $ {tip:.2f}\n\
Total : $ {total:.2f}\n\n\
Hope to see you again soon!"
    print(output)


#######################
# Henry's edits (end)
#######################

def main():
    # heading for program
    printHeading()

    # ask for 1st diner's drink, entree and dessert
    print("------------------------------------------------------")
    drink1 = input("Enter drink order for diner #1:   ")
    drink1Price = eval(input("Enter drink price for diner #1:   "))
    entree1 = input("Enter entree order for diner #1:  ")
    entree1Price = eval(input("Enter entree price for diner #1:  "))
    dessert1 = input("Enter dessert order for diner #1: ")
    dessert1Price = eval(input("Enter dessert price for diner #1: "))
    print()

    # ask for 2nd diner's drink, entree and dessert
    print("------------------------------------------------------")
    drink2 = input("Enter drink order for diner #2:   ")
    drink2Price = eval(input("Enter drink price for diner #2:   "))
    entree2 = input("Enter entree order for diner #2:  ")
    entree2Price = eval(input("Enter entree price for diner #2:  "))
    dessert2 = input("Enter dessert order for diner #2: ")
    dessert2Price = eval(input("Enter dessert price for diner #2: "))
    print()

    # ask for local tax rate
    taxRate = getTaxPercent()

    # ask for tip % to use
    tipPercent = getTipPercent()

    # separate print before customer bills
    print()

    # print bills for customers
    printBill(1,drink1,drink1Price,
              entree1,entree1Price,
              dessert1,dessert1Price,
              taxRate,tipPercent)
    print()
    printBill(2,drink2,drink2Price,
              entree2,entree2Price,
              dessert2,dessert2Price,
              taxRate,tipPercent)


main()
