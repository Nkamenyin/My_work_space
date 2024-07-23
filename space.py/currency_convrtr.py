#!/usr/bin/python3

""" creating a currency converter Hirak API as my external Api and using currency_converter.py as it's module"""

import currency_converter

amount = float(input("Enter amount: "))
from_currency = input("From currency (NGN, USD, EUR, GBP, JPY): ")
to_currency = input("To currency (NGN, USD, EUR, GBP, JPY): ")

result = currency_converter.convert_and_format(amount, from_currency, to_currency)
print(result)
