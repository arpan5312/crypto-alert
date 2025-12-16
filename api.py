import requests

def get_price(coin_id, currency_id):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": currency_id
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Status error:", response.status_code)
        return None  

    data = response.json()

    
    try:
        price = data[coin_id][currency_id]
        return price
    except KeyError:
        print("Invalid coin or currency")
        return None

