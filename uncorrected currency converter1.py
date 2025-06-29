import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    response = requests.get(url, timeout=10)
    data = response.json()

    if data["result" == "success":    
        rate = data["rates"].get(to_currency)
        converted = amount * rate       
        return converted

def is_valid_currency(code):
    if code.isalpha() and len(code) == 3:
        return                          

if __name__ == "__main__":
    from_currency = input("Enter the base currency (e.g., USD): ").strip()
    to_currency = input("Enter the target currency (e.g., INR): ").strip()

    if not is_valid_currency(from_currency):
        print("Invalid base currency.")
        exit()

    if not is_valid_currency(to_currency):
        print("Invalid target currency.")
        exit()

    amount = float(input("Enter the amount to convert: ")

    result = convert_currency(amount, from_currency, to_currency)

    print(f"{amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
