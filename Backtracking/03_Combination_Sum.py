"""
LeetCode #39: Combination Sum
Category: Backtracking
Difficulty: Medium

Problem:
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.

Example:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

LEARNING FOCUS:
- Backtracking with target
- Reusing elements
- Avoiding duplicates
"""

from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    
    result = []
    candidates.sort()  # Sort to help pruning
    
    def backtrack(start: int, remaining: int, current: List[int]):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break  # Pruning: no need to continue
            
            # Include candidates[i]
            current.append(candidates[i])
            
            # Recurse (can reuse same element, so i not i+1)
            backtrack(i, remaining - candidates[i], current)
            
            # Backtrack
            current.pop()
    
    backtrack(0, target, [])
    return result


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
        ([2], 1),
    ]
    
    for candidates, target in test_cases:
        result = combination_sum(candidates, target)
        print(f"candidates={candidates}, target={target}")
        print(f"Combinations ({len(result)} total):")
        for combo in result:
            print(f"  {combo}")
        print()
