import requests

def convert_currency(amount, from_currency, to_currency):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    
    url = "https://open.er-api.com/v6/latest/{from_currency}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("result") != "success":
            print(" API error:", data.get("error-type", "Unknown error"))
            return None

        rates = data.get("rates", {})
        if to_currency not in rates:
            print(" Target currency {to_currency} not found in rates.")
            return None

        converted = amount * rates[to_currency]
        return converted

    except requests.RequestException as e:
        print(" Network error: {e}")
        return None

def is_valid_currency(code):
    return code.isalpha() and len(code) == 3

if __name__ == "__main__":
    from_currency = input("Enter the base currency (e.g., USD): ").strip()
    to_currency = input("Enter the target currency (e.g., INR): ").strip()

    if not is_valid_currency(from_currency):
        print(" Invalid base currency code.")
        exit()

    if not is_valid_currency(to_currency):
        print(" Invalid target currency code.")
        exit()

    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print(" Invalid amount. Please enter a number.")
        exit()

    result = convert_currency(amount, from_currency, to_currency)
    if result is not None:
        print(f"\n✅ {amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
    else:
        print("\n Conversion failed.")
