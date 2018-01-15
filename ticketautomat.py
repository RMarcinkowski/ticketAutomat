from __future__ import print_function
import sys
from decimal import *
import locale
locale.setlocale(locale.LC_ALL, "de-DE")

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# define cash class and create the money used in the automat
class Cash:
    def __init__(self, value, quantity):
        self.value = value
        self.quantity = quantity

oneCent = Cash(1, 50)
twoCent = Cash(2, 50)
fiveCent = Cash(5, 20)
tenCent = Cash(10, 20)
twentyCent = Cash(20, 20)
fiftyCent = Cash(50, 20)
oneEuro = Cash(100, 20)
twoEuro = Cash(200, 20)
fiveEuro = Cash(500, 10)
tenEuro = Cash(1000, 50)
twentyEuro = Cash(2000, 50)

cashArray = [twentyEuro, tenEuro, fiveEuro, twoEuro, oneEuro, fiftyCent, twentyCent, tenCent, fiveCent, twoCent,
             oneCent]
changeArray = []

# try if the specific cash can be used as change and if so, use it
def tryCash(cash, change):
    if (cash.value <= change and cash.quantity > 0):
        cash.quantity -= 1
        changeArray.append(cash)
        return True
    return False

# main program
runProgram = True
while runProgram:

    # clear the changeArray and freeze the current cash status
    changeArray = []
    currentCashArray = []
    for i in range(len(cashArray)):
        currentCashArray.append(cashArray[i].quantity)

    # get input and check for correctness, repeat until everything is correct
    correctInput = False
    while not correctInput:
        price = input("Gib den Preis in Euro ein: ")
        try:
            price = Decimal(price)
            if price > 0:
                correctInput = True
            else:
                print("Der Preis muss eine positive Zahl sein.")
        except:
            if ',' in price:
                print("Dezimalzahlen müssen durch einen Punkt getrennt werden.")
            else:
                print("Der Preis muss eine Zahl sein.")

    correctInput = False
    while not correctInput:
        money = input("Gib den bezahlten Geldbetrag in Euro ein: ")
        try:
            money = Decimal(money)
            if money >= price:
                correctInput = True
            else:
                print("Der Geldbetrag muss größer oder gleich dem Preis sein.")
        except:
            if ',' in money:
                print("Dezimalzahlen müssen durch einen Punkt getrennt werden.")
            else:
                print("Der Geldbetrag muss eine Zahl sein.")

    # translate money input to cent-based money
    money = money * 100
    price = price * 100

    # calculate change
    change = money - price
    while change > 0:
        cashUsed = False
        for i in range(len(cashArray)):
            if (tryCash(cashArray[i], change)):
                change -= cashArray[i].value
                cashUsed = True
                break
        if not cashUsed:
            print("Der Automat scheint nicht genug Geld zu haben.")
            quit()
    for i in range(len(changeArray)):
        change += changeArray[i].value

    # check change for correctness
    if (price + change != money):
        print("Fehler im Programm")

    # print the results
    print("\n\nIhr Wechselgeld beträgt: " + str(locale.currency(change / 100)))
    print("Und besteht aus:")
    for i in range(len(cashArray)):
        if (currentCashArray[i] - cashArray[i].quantity > 0):
            print(str(currentCashArray[i] - cashArray[i].quantity) + "mal " + str(
                locale.currency(cashArray[i].value / 100)))

    # print the remaining cash in the automat to stderr
    eprint("\nEs sind noch folgende Geldbeträge im Automaten:")
    for i in range(len(cashArray)):
        eprint(str(locale.currency(cashArray[i].value / 100)) + ": " + str(cashArray[i].quantity) + "mal")

    # ask for repetition
    repeat = input("\n\nDas Ticket wurde erfolgreich gekauft. Weiteres Ticket kaufen? 'j' eingeben")
    if repeat != "j":
        runProgram = False

print("Auf Wiedersehen und gute Fahrt!")
