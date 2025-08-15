# stock_buy_sell.py
"""
Stock Buy and Sell Problem

Problem:
- You are given an array 'prices' where prices[i] is the stock price on day i.
- You can buy and sell multiple times (cannot hold more than 1 stock at a time).
- Goal: Maximize total profit.

Example:
prices = [7, 1, 5, 3, 6, 4]
Optimal Transactions:
  Buy on day 1 (price=1), Sell on day 2 (price=5) → profit=4
  Buy on day 3 (price=3), Sell on day 4 (price=6) → profit=3
Total Profit = 7
"""

# -------------------------------
# Approach 1: Brute Force
# -------------------------------
def maxProfitBrute(prices):
    """
    Brute Force Approach
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(prices)          # Total days
    max_profit = 0           # Initialize profit

    # Try all buy-sell pairs
    for i in range(n-1):          # Buy day
        for j in range(i+1, n):   # Sell day
            if prices[j] > prices[i]:         # Only profitable transactions
                profit = prices[j] - prices[i]
                max_profit += profit           # Add to total

    return max_profit

# -------------------------------
# Approach 2: Greedy / Efficient
# -------------------------------
def maxProfit(prices):
    """
    Greedy / Efficient Approach
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    max_profit = 0

    # Add profit for every upward movement
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            max_profit += prices[i+1] - prices[i]

    return max_profit

# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]

    profit_brute = maxProfitBrute(prices)
    profit_greedy = maxProfit(prices)

    print("Stock Prices:", prices)
    print("Maximum Profit (Brute Force):", profit_brute)
    print("Maximum Profit (Greedy / Efficient):", profit_greedy)
