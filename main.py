from currency_converter import CurrencyConverter

c = CurrencyConverter()
amount = 180
from_currency = 'JPY'
to_currency = 'EUR'
converted_amount = c.convert(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

#use some library that has the database of all currencies(symbols and abbreviations and names)
#that make a simple addon fronted code(selected text gets converted)