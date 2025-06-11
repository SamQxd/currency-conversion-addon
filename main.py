from currency_converter import CurrencyConverter
import pycountry
from get_currency_code import get_currency_code

#for currency in pycountry.currencies:
#    print(f"Name: {currency.name}, Code: {currency.alpha_3}")

test_inputs = [
    ("US Dollar", None),       # Correct name
    ("$", "Australia"),        # Symbol with country context
    ("Euro", None),            # Name
    ("€", None),               # Symbol
    ("Yen", None),             # Correct name
    ("¥", "Japan"),               # Symbol
    ("Maldivian Rufiyaa", None),  # Name
    ("£", None),               # Symbol
    ("$", "Australia"),        # Symbol with country context
]

for input_str, country in test_inputs:
    code = get_currency_code(input_str, country)
    print(f"Input: {input_str}, Code: {code}")

c = CurrencyConverter()
amount = 180
from_currency = 'JPY'
to_currency = 'EUR'
converted_amount = c.convert(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

#use some library that has the database of all currencies(symbols and abbreviations and names)
#that make a simple addon fronted code(selected text gets converted)