import sys
from decimal import *
import locale

locale.setlocale(locale.LC_ALL, "de-DE")

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

cashArray = [twentyEuro, tenEuro, fiveEuro, twoEuro, oneEuro, 
             fiftyCent, twentyCent, tenCent, fiveCent, twoCent, oneCent]
changeArray = []
# try if the specific cash can be used as change and if so, use it
def tryCash(cash, change):
    if (cash.value <= change and cash.quantity > 0):
        cash.quantity -= 1
        changeArray.append(cash)
        return True
    return False

# validate both inputs
def validateInput(value):
  try:
    value = Decimal(value)
    if value > 0:
      return "valid"
    else:
      return "Es muss eine positive Zahl sein."
  except:
    if ',' in value:
      return "Dezimalzahlen müssen durch einen Punkt getrennt werden."
    else:
      return "Es muss eine Zahl sein."

def validateMoneyInput(money, price):
  if money >= price:
    return "valid"
  else:
    return "Der Geldbetrag muss größer oder gleich dem Preis sein."


# main program
def calcChange(price, money): 
  
  # clear the changeArray and freeze the current cash status
  del changeArray[:]
  currentCashArray = []
  for i in range(len(cashArray)):
      currentCashArray.append(cashArray[i].quantity)
  
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
  print("\nEs sind noch folgende Geldbeträge im Automaten:", file=sys.stderr)
  for i in range(len(cashArray)):
      print(str(locale.currency(cashArray[i].value / 100)) + ": " + str(cashArray[i].quantity) + "mal", file=sys.stderr)
  
  return change/100