from api import get_price
from storage import data_storage
from logic import percent_change

price_data = data_storage()
price_data = data_storage()

change = percent_change(
    price_data["old_price"],
    price_data["current_price"]
)

print("Percent change:", change)

