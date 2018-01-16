from decimal import *
from TicketAutomat import *
from GetGreeting import printInfo

printInfo("'Ticketautomat'", "1.1", "Ruben Marcinkowski")

runProgram = True
while runProgram:

    #get input and check for correctness, repeat until everything is correct    
    userInput = ""
    while userInput != "valid":
      price = input("Gib den Preis in Euro ein: ")
      userInput = validateInput(price)
      if userInput != "valid":
        print(userInput)
    price = Decimal(price)
    
   
    userInput = ""
    while userInput != "valid":
      money = input("Gib den bezahlten Geldbetrag in Euro ein: ")
      userInput = validateInput(money)
      if userInput == "valid":
        userInput = validateMoneyInput(Decimal(money), price)
        if userInput != "valid":
          print(userInput)
      else:
        print(userInput)
    money = Decimal(money)

    # calculate the change
    calcChange(price, money)
    
    # ask for repetition
    repeat = input("\n\nDas Ticket wurde erfolgreich gekauft. Weiteres Ticket kaufen? 'j' eingeben")
    if repeat != "j":
      runProgram = False
  
print("Auf Wiedersehen und gute Fahrt!")