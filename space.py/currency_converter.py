import requests

"""this api end point will require input of from_to currency e.g 
https://rates.hirak.site/USD_NGN/"""

def get_exchange_rates(base_currency):
    response = requests.get(f"(https://rates.hirak.site/)")
    data = response.json()
    return data["rates"]

def convert_currency(amount, from_currency, to_currency):
    exchange_rates = get_exchange_rates(from_currency)
    if to_currency in exchange_rates:
        return amount * exchange_rates[to_currency]
    else:
        return None

def format_output(amount, currency):
    symbol = {"NGN":"#", "USD": "$", "EUR": "€", "GBP": "£", "JPY": "¥"}[currency]
    return f"{symbol}{amount:.2f}"

def convert_and_format(amount, from_currency, to_currency):
    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount:
        return format_output(converted_amount, to_currency)
    else:
        return "Unable to convert"
