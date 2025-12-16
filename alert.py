"""detects price abnormality by testing whether the move is outside what this asset has recently proven it can do normally"""

from storage import price_memory
from logic import percent_change

prices: list[float]        
timestamps: list[int]    


returns = [
    (percent_change())
]