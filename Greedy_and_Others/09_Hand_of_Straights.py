"""
LeetCode #846: Hand of Straights
Category: Greedy & Others
Difficulty: Medium

Problem:
Alice has some number of cards and she wants to rearrange the cards into groups
so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card
and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

LEARNING FOCUS:
- Greedy grouping
- Counting and consecutive sequences
"""

from typing import List
from collections import Counter


def is_straight_hand(hand: List[int], group_size: int) -> bool:
    
    if len(hand) % group_size != 0:
        return False
    
    count = Counter(hand)
    
    for card in sorted(count):
        if count[card] > 0:
            # Need to form groups starting from this card
            needed = count[card]
            
            for i in range(card, card + group_size):
                if count[i] < needed:
                    return False
                count[i] -= needed
    
    return True


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 6, 2, 3, 4, 7, 8], 3, True),
        ([1, 2, 3, 4, 5], 4, False),
    ]
    
    for hand, group_size, expected in test_cases:
        result = is_straight_hand(hand, group_size)
        print(f"hand={hand}, groupSize={group_size}")
        print(f"  Can form: {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
