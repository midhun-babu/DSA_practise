"""
LeetCode #322: Coin Change
Category: Dynamic Programming
Difficulty: Medium

Problem:
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

LEARNING FOCUS:
- Unbounded knapsack problem
- Bottom-up DP
- Minimization DP
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    """
    Minimum coins needed to make amount.
    
    THE INTUITION:
    dp[i] = minimum coins to make amount i
    
    For each amount, try all coins:
    dp[i] = min(dp[i], dp[i - coin] + 1) for each coin
    
    Time: O(amount × len(coins))
    Space: O(amount)
    """
    # Initialize with amount + 1 (impossible value)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # 0 coins needed for amount 0
    
    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(
                    dp[current_amount],
                    dp[current_amount - coin] + 1
                )
    
    return dp[amount] if dp[amount] <= amount else -1


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
        ([1], 1, 1),
        ([1], 2, 2),
    ]
    
    for coins, amount, expected in test_cases:
        result = coin_change(coins, amount)
        print(f"coins={coins}, amount={amount}")
        print(f"  Min coins: {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
