"""
LeetCode #121: Best Time to Buy and Sell Stock
Category: Arrays & Strings
Difficulty: Easy

Problem:
Given an array prices where prices[i] is the price of a stock on day i,
return the maximum profit you can achieve from one transaction.
If you cannot achieve any profit, return 0.

Example:
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price=1), sell on day 5 (price=6), profit=5.

LEARNING FOCUS:
- One-pass algorithm
- Tracking minimum and maximum simultaneously
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Find maximum profit from buying and selling stock once.
    
    THE INTUITION:
    We want to buy low and sell high. As we go through each day:
    1. Track the minimum price we've seen so far (best day to buy)
    2. Calculate profit if we sell today
    3. Update max profit if this is better
    
    Time: O(n) - single pass
    Space: O(1) - just two variables
    """
    if len(prices) < 2:
        return 0
    
    min_price = prices[0]  # Best price to buy so far
    max_profit_so_far = 0
    
    for price in prices:
        # Update minimum price if today is cheaper
        if price < min_price:
            min_price = price
        
        # Calculate profit if we sell today
        profit = price - min_price
        
        # Update max profit
        max_profit_so_far = max(max_profit_so_far, profit)
    
    return max_profit_so_far


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2, 3, 4, 5], 4),
    ]
    
    for prices, expected in test_cases:
        result = max_profit(prices)
        print(f"prices={prices}")
        print(f"  Result: {result}, Expected: {expected}")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
