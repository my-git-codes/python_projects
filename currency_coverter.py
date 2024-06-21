import requests

def get_exchange_rate(api_key, from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print("Error fetching exchange rates")
        return None

    try:
        rate = data['conversion_rates'][to_currency]
        return rate
    except KeyError:
        print(f"Invalid currency code: {to_currency}")
        return None

def convert_currency(api_key, amount, from_currency, to_currency):
    rate = get_exchange_rate(api_key, from_currency, to_currency)
    if rate is not None:
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

if __name__ == "__main__":
    api_key = "bce3b3e2efa556156aaec595"
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (e.g., USD): ").upper()
    to_currency = input("To currency (e.g., EUR): ").upper()

    result = convert_currency(api_key, amount, from_currency, to_currency)
    if result is not None:
        print(f"{amount} {from_currency} is {result:.2f} {to_currency}")
    else:
        print("Conversion failed.")
