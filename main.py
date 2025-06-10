from currency_converter import CurrencyConverter

c = CurrencyConverter()
amount = 180
from_currency = 'JPY'
to_currency = 'EUR'
converted_amount = c.convert(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")