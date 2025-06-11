import pycountry
from forex_python.converter import CurrencyCodes

def get_currency_code(input_str, country=None):
    """
    Convert a currency name or symbol to its ISO 4217 code (e.g., USD, EUR).
    Returns the code or None if not found. Uses country context for ambiguous symbols like $.
    """
    c = CurrencyCodes()

    # Step 1: Try matching as a currency name
    try:
        # Normalize input: strip whitespace and convert to title case
        normalized_input = input_str.strip().title()
        currency = pycountry.currencies.lookup(normalized_input)
        return currency.alpha_3
    except LookupError:
        pass

    # Step 2: Try matching as a currency symbol
    # Handle country context for $
    country_currency_map = {
        "United States": "USD",
        "Australia": "AUD",
        "Canada": "CAD",
        "New Zealand": "NZD",
        "Singapore": "SGD",
        "Hong Kong": "HKD",
        "Bahamas": "BSD",
        "Fiji": "FJD",
        "Barbados": "BBD",
        "Jamaica": "JMD",
    }

    # Check country context for $
    if input_str == "$" and country and country in country_currency_map:
        return country_currency_map[country]

    # Fallback: Check all currencies for symbol match
    possible_codes = []
    for currency in pycountry.currencies:
        symbol = c.get_symbol(currency.alpha_3)
        if symbol == input_str:
            possible_codes.append(currency.alpha_3)

    if possible_codes:
        # Return first match for ambiguous symbols
        return possible_codes[0]

    return None