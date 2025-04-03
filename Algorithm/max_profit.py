def max_profit(prices):
    min_buy = float('inf')
    maximum_profit = 0
    
    for price in prices:
        min_buy = min(min_buy, price)
        maximum_profit = max(maximum_profit, price - min_buy)
            
    return maximum_profit