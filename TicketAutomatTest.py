from decimal import *
import unittest
from TicketAutomat import *

class TicketAutomatTest(unittest.TestCase):
    
    def test_InputString(self):
        self.assertEqual(validateInput("one"), "Es muss eine Zahl sein.")
    def test_InputWrongDecimalSign(self):
        self.assertEqual(validateInput("1,2"), "Dezimalzahlen müssen durch einen Punkt getrennt werden.")
    def test_InputNegative(self):
        self.assertEqual(validateInput("-1.2"), "Es muss eine positive Zahl sein.")
    def test_InputValid(self):
        self.assertEqual(validateInput("1.2"), "valid")

    def test_MoneySmallerPrice(self):
        self.assertEqual(validateMoneyInput(1, 2), "Der Geldbetrag muss größer oder gleich dem Preis sein.")
    def test_MoneyEqualsPrice(self):
        self.assertEqual(validateMoneyInput(1, 1), "valid")
    def test_MoneyGreaterPrice(self):
        self.assertEqual(validateMoneyInput(1.1, 1), "valid")


    def test_calcChange1(self):
      self.assertEqual(calcChange(Decimal("2.22"), Decimal("3")), Decimal("0.78"))
    def test_calcChange2(self):
      self.assertEqual(calcChange(Decimal("1.09"), Decimal("100")), Decimal("98.91"))

if __name__ == '__main__':
    unittest.main()