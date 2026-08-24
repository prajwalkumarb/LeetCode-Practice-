# Problem: You're given an array prices where prices[i] is the price of a stock on day i. 
#           You want to maximize your profit by choosing a single day to buy and a different (later) day to sell.
#           Return the maximum profit. If no profit is possible, return 0.

# Example:
# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 5   // buy on day 1 (price=1), sell on day 4 (price=6), profit = 5
# Hint: As you scan left to right, at each day you only care about two things: 
#   the lowest price you've seen so far, and the best profit you could make if you sold today (current price − lowest price so far). 
#   You don't need nested loops — just track a running minimum and a running max profit as you go.


# Let's manually check a few options from the example:

# Buy day 1 (price 1), sell day 2 (price 5) → profit = 4
# Buy day 1 (price 1), sell day 4 (price 6) → profit = 5 ✅ best one
# Buy day 3 (price 3), sell day 4 (price 6) → profit = 3
# Buy day 0 (price 7), sell day 1 (price 1) → profit = -6, not allowed to lose money by choice — if nothing works out, answer is 0


def ret_max_profit(prices):
    max_profit = 0
    min_price = prices[0]
    for i in prices:
        if i < min_price:
            min_price = i
        
        profit = i - min_price 
        if profit > max_profit:
            max_profit = profit
    return max_profit


if __name__ == "__main__":
    result = ret_max_profit([7, 1, 5, 3, 6, 4])
    print(result)