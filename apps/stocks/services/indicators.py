def calculate_sma(prices, period=14):
    if len(prices) < period:
        return None
    return sum(prices[-period:]) / period
