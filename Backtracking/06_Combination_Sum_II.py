"""
LeetCode #40: Combination Sum II
Category: Backtracking
Difficulty: Medium

Problem:
Given a collection of candidate numbers candidates and a target number target,
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

LEARNING FOCUS:
- Handling duplicates
- Skip logic
- Sorting to group duplicates
"""

from typing import List


def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:
    
    result = []
    candidates.sort()
    
    def backtrack(start: int, remaining: int, current: List[int]):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            # Skip duplicates at the same level
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            if candidates[i] > remaining:
                break
            
            current.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i], current)  # i+1: can't reuse
            current.pop()
    
    backtrack(0, target, [])
    return result


# ============== TEST ==============
if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    result = combination_sum2(candidates, target)
    print(f"candidates = {candidates}")
    print(f"target = {target}")
    print(f"Combinations ({len(result)} total):")
    for combo in result:
        print(f"  {combo}")
