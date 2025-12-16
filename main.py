import time
from storage import computation
from alert import check_alert
from api import get_price

#asset:
COIN_ID = "bitcoin"      
CURRENCY_ID = "usd"
ASSET_NAME = "BTC"
POLL_INTERVAL = 300 


while True:
    price = get_price(COIN_ID,CURRENCY_ID)
    if price is not None:
        computation(price)
        check_alert(ASSET_NAME)

    else:
        print("price fetch failed, skipping this interval...")


    print(f"Latest price: {price}")

    time.sleep(POLL_INTERVAL)
    