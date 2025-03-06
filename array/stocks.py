def maximumProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
            print(profit)
    return profit


prices = [100, 180, 260, 310, 40, 535, 695]
print(maximumProfit(prices))

# 310 - 100 = 210
# 695 - 100 = 595