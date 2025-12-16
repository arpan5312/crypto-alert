from logic import percent_change
prices = []
returns = []
max_history = 20
baseline_volume = None

def computation (new_price):
    prices.append(new_price)

    #return
    if len(prices)>=2:
        r = percent_change(prices[-2],prices[-1])
        if r is not None:
            returns.append(r)


    #maintaining rolling window
    if len(prices) > max_history:
        prices.pop(0)
    if len(returns) > max_history:
        prices.pop(0)

    #mainting baseline
    if len(returns)%3 == 0:
        baseline_operations()

def baseline_operations():
    global baseline_volume

    if returns:
        recent = returns[-max_history]
        baseline_volume = sum(abs(r) for r in recent) / len(recent)

        

def get_latest_return():
    if returns:
        latest_return = returns[-1]
        return latest_return
    else:
        return None