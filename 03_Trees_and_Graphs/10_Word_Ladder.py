"""
LeetCode #127: Word Ladder
Category: Trees & Graphs
Difficulty: Hard

Problem:
A transformation sequence from word beginWord to word endWord using a dictionary wordList
is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair differs by exactly one letter
- Every si is in wordList
- sk == endWord

Return the number of words in the shortest transformation sequence,
or 0 if no such sequence exists.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: hit -> hot -> dot -> dog -> cog

LEARNING FOCUS:
- BFS for shortest path
- Word transformation graph
- Bidirectional BFS optimization
"""

from typing import List
from collections import deque, defaultdict


def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    """
    Find shortest transformation sequence length using BFS.
    
    THE INTUITION:
    Treat each word as a node. Two words are connected if they differ by one letter.
    Use BFS to find shortest path from begin_word to end_word.
    
    Time: O(N × M²) where N = word count, M = word length
    Space: O(N × M)
    """
    if end_word not in word_list:
        return 0
    
    word_set = set(word_list)
    queue = deque([(begin_word, 1)])
    
    while queue:
        word, length = queue.popleft()
        
        if word == end_word:
            return length
        
        # Try all possible one-letter transformations
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                
                if new_word in word_set:
                    word_set.remove(new_word)  # Mark as visited
                    queue.append((new_word, length + 1))
    
    return 0


def ladder_length_bidirectional(begin_word: str, end_word: str, word_list: List[str]) -> int:
    """
    Bidirectional BFS - faster in practice.
    
    Search from both ends simultaneously. When searches meet, we found the path.
    
    Time: O(N × M²) but often faster
    Space: O(N × M)
    """
    if end_word not in word_list:
        return 0
    
    word_set = set(word_list)
    
    # Two frontiers
    begin_set = {begin_word}
    end_set = {end_word}
    
    length = 1
    
    while begin_set and end_set:
        # Always expand the smaller frontier
        if len(begin_set) > len(end_set):
            begin_set, end_set = end_set, begin_set
        
        next_set = set()
        
        for word in begin_set:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    
                    if new_word in end_set:
                        return length + 1
                    
                    if new_word in word_set:
                        word_set.remove(new_word)
                        next_set.add(new_word)
        
        begin_set = next_set
        length += 1
    
    return 0


# ============== TEST ==============
if __name__ == "__main__":
    begin = "hit"
    end = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    
    print(f"BFS: {ladder_length(begin, end, word_list)}")  # 5
    print(f"Bidirectional: {ladder_length_bidirectional(begin, end, word_list)}")  # 5
