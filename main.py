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

price_memory = {
    "old_price": None,
    "current_price" : None

}
def data_storage():
    new_price = get_price("bitcoin","usd")
    if new_price is not None:
        
        price_memory["old_price"] = price_memory["current_price"]
        
        
        price_memory["current_price"] = new_price
    return price_memory.copy()



def percent_change(old,new):
       

    if old is None or new is None:
        return None
    if old == 0:
        return None

    try:
        change = ((float(new) - float(old)) / float(old)) * 100
        return change
    except TypeError:
        return None



price_data = data_storage()
print("First run:", price_data)

price_data = data_storage()
change = percent_change(
    price_data["old_price"],
    price_data["current_price"]
)

print("Second run:", price_data)
print("Percent change:", change)
