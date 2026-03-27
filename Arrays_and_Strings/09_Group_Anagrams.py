"""
LeetCode #49: Group Anagrams
Category: Arrays & Strings
Difficulty: Medium

Problem:
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word
or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

LEARNING FOCUS:
- Hash Map with custom keys
- Sorting as signature
- Character counting
"""

from typing import List
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams together.
    
    THE INTUITION:
    Anagrams have the same sorted characters. So we can use the sorted string
    as a "signature" or key in a hash map.
    
    Time: O(n × k log k) where n = number of strings, k = max string length
    Space: O(n × k)
    """
    groups = defaultdict(list)
    
    for s in strs:
        # Sort the string to get signature
        signature = ''.join(sorted(s))
        groups[signature].append(s)
    
    return list(groups.values())


def group_anagrams_count(strs: List[str]) -> List[List[str]]:
    """
    Alternative: Use character count as signature.
    
    Time: O(n × k) - faster for long strings
    Space: O(n × k)
    """
    groups = defaultdict(list)
    
    for s in strs:
        # Count characters (26 lowercase letters)
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        # Use tuple as key (lists can't be dict keys)
        signature = tuple(count)
        groups[signature].append(s)
    
    return list(groups.values())


# ============== TEST ==============
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(strs)
    print(f"strs={strs}")
    print(f"Result: {result}")
    
    # Verify all anagrams are grouped
    for group in result:
        print(f"  Group: {group}")
    print()
