"""
LeetCode #134: Gas Station
Category: Greedy & Others
Difficulty: Medium

Problem:
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station
to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel
around the circuit once in the clockwise direction, otherwise return -1.

LEARNING FOCUS:
- Greedy proof
- Tracking tank and total
"""

from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    
    total_gas = 0
    total_cost = 0
    tank = 0
    start = 0
    
    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]
        
        # Can't reach station i+1 from start
        if tank < 0:
            start = i + 1
            tank = 0
    
    return start if total_gas >= total_cost else -1


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),
    ]
    
    for gas, cost, expected in test_cases:
        result = can_complete_circuit(gas, cost)
        print(f"gas={gas}, cost={cost}")
        print(f"  Start: {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
