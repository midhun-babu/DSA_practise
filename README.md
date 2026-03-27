# DSA Preparation - LeetCode Style Questions (By Category)

This folder contains a curated collection of **80+ Data Structures and Algorithms (DSA) questions** organized by **category** to help you prepare for technical interviews.

## Why Category-Based Organization?

Instead of organizing by difficulty, this structure helps you:
- **Master patterns** within each topic
- **Focus your practice** on weak areas
- **Build intuition** for specific problem types
- **Recognize patterns** quickly in interviews

---

## Folder Structure

```
DSA_Preparation/
├── 01_Arrays_and_Strings/      # 10 problems
├── 02_Linked_Lists/            # 5 problems
├── 03_Trees_and_Graphs/        # 10 problems
├── 04_Dynamic_Programming/     # 10 problems
├── 05_Sorting_and_Searching/   # 10 problems
├── 06_Backtracking/            # 10 problems
├── 07_Design_Problems/         # 5 problems
├── 08_Greedy_and_Others/       # 10 problems
└── README.md
```

---

## Category Breakdown

### 01. Arrays & Strings (10 Problems)
| # | Problem | Key Pattern |
|---|---------|-------------|
| 01 | Two Sum | Hash Map |
| 02 | Best Time to Buy/Sell Stock | One-pass Tracking |
| 03 | Contains Duplicate | Hash Set |
| 04 | Product of Array Except Self | Prefix/Suffix |
| 05 | Maximum Subarray (Kadane's) | DP on Array |
| 06 | Longest Substring Without Repeating | Sliding Window |
| 07 | 3Sum | Two Pointers |
| 08 | Valid Palindrome | Two Pointers |
| 09 | Group Anagrams | Hash Map with Signature |
| 10 | Minimum Window Substring | Sliding Window |

**Study Focus:** Sliding window, two pointers, hash map techniques

---

### 02. Linked Lists (5 Problems)
| # | Problem | Key Pattern |
|---|---------|-------------|
| 01 | Reverse Linked List | Pointer Manipulation |
| 02 | Merge Two Sorted Lists | Two Pointers |
| 03 | Linked List Cycle | Floyd's Algorithm |
| 04 | Remove Nth Node From End | Fast/Slow Pointers |
| 05 | Reorder List | Multiple Techniques |

**Study Focus:** Pointer manipulation, fast/slow pointers, reversal

---

### 03. Trees & Graphs (10 Problems)
| # | Problem | Key Pattern |
|---|---------|-------------|
| 01 | Invert Binary Tree | DFS/BFS |
| 02 | Maximum Depth of Binary Tree | Recursion |
| 03 | Same Tree | Tree Comparison |
| 04 | Number of Islands | DFS/BFS on Grid |
| 05 | Course Schedule | Topological Sort |
| 06 | Clone Graph | Graph Traversal |
| 07 | Binary Tree Level Order | BFS |
| 08 | Lowest Common Ancestor BST | BST Properties |
| 09 | Binary Tree Maximum Path Sum | Post-order DFS |
| 10 | Word Ladder | BFS Shortest Path |

**Study Focus:** DFS, BFS, tree traversals, graph algorithms

---

### 04. Dynamic Programming (10 Problems)
| # | Problem | Key Pattern |
|---|---------|-------------|
| 01 | Climbing Stairs | Fibonacci DP |
| 02 | House Robber | Decision DP |
| 03 | Coin Change | Unbounded Knapsack |
| 04 | Longest Increasing Subsequence | LIS Pattern |
| 05 | Word Break | String DP |
| 06 | Longest Palindromic Substring | Expand Around Center |
| 07 | Edit Distance | 2D DP |
| 08 | Regular Expression Matching | Complex DP |
| 09 | Unique Paths | Grid DP |
| 10 | Decode Ways | String DP |

**Study Focus:** State definition, transitions, space optimization

---

### 05. Sorting & Searching (10 Problems)
| # | Problem | Key Pattern |
|---|---------|-------------|
| 01 | Binary Search | Classic BS |
| 02 | Search in Rotated Sorted Array | Modified BS |
| 03 | Find Minimum in Rotated Array | BS with Pivot |
| 04 | Kth Largest Element | QuickSelect/Heap |
| 05 | Median of Two Sorted Arrays | BS on Partitions |
| 06 | Merge Intervals | Sort + Greedy |
| 07 | Insert Interval | Three-Phase |
| 08 | Non-overlapping Intervals | Greedy |
| 09 | Meeting Rooms II | Min-Heap |
| 10 | Rotate Image | Matrix Operation |

**Study Focus:** Binary search variations, interval problems

---

### 06. Backtracking (10 Problems)
| # | Problem | Key Pattern |
|---|---------|-------------|
| 01 | Subsets | Include/Exclude |
| 02 | Permutations | Swap/Used Array |
| 03 | Combination Sum | Reuse Elements |
| 04 | N-Queens | Constraint Tracking |
| 05 | Generate Parentheses | Count Tracking |
| 06 | Combination Sum II | Skip Duplicates |
| 07 | Palindrome Partitioning | String Partition |
| 08 | Letter Combinations of Phone | Multiple Choice |
| 09 | Word Search | 2D Grid |
| 10 | Sudoku Solver | Complex Constraints |

**Study Focus:** Decision trees, pruning, state backtracking

---

### 07. Design Problems (5 Problems)
| # | Problem | Key Pattern |
|---|---------|-------------|
| 01 | LRU Cache | Hash + LinkedList |
| 02 | Min Stack | Auxiliary Tracking |
| 03 | Design HashMap | Chaining |
| 04 | Design Circular Queue | Array + Pointers |
| 05 | Trie (Prefix Tree) | Tree Structure |

**Study Focus:** Data structure combinations, O(1) operations

---

### 08. Greedy & Others (10 Problems)
| # | Problem | Key Pattern |
|---|---------|-------------|
| 01 | Valid Parentheses | Stack |
| 02 | Jump Game | Greedy |
| 03 | Gas Station | Greedy Proof |
| 04 | Trapping Rain Water | Two Pointers |
| 05 | Longest Valid Parentheses | Stack/DP |
| 06 | Wildcard Matching | Two Pointers |
| 07 | Merge k Sorted Lists | Heap/D&C |
| 08 | Task Scheduler | Greedy + Math |
| 09 | Hand of Straights | Greedy Grouping |
| 10 | Sliding Window Maximum | Monotonic Deque |

**Study Focus:** Greedy choices, monotonic structures

---

## How to Use This Repository

### 1. Start with Fundamentals
Begin with **Arrays & Strings** and **Linked Lists** - these form the foundation.

### 2. Build Core Skills
Move to **Trees & Graphs** and **Sorting & Searching** - interview staples.

### 3. Master Advanced Topics
Tackle **Dynamic Programming** and **Backtracking** - differentiate yourself.

### 4. Polish with Design
Study **Design Problems** - common in senior interviews.

---

## Running the Code

Each Python file is self-contained:

```bash
# Arrays & Strings
python 01_Arrays_and_Strings/01_Two_Sum.py
python 01_Arrays_and_Strings/06_Longest_Substring_Without_Repeating.py

# Trees & Graphs
python 03_Trees_and_Graphs/04_Number_of_Islands.py

# Dynamic Programming
python 04_Dynamic_Programming/03_Coin_Change.py

# Backtracking
python 06_Backtracking/04_N_Queens.py
```

Each file includes:
- Problem description
- Multiple approaches (where applicable)
- Human-friendly comments
- Time/space complexity analysis
- Test cases

---

## Key Patterns Summary

### Must-Know Patterns
| Pattern | Problems |
|---------|----------|
| Two Pointers | Two Sum, 3Sum, Valid Palindrome |
| Sliding Window | Longest Substring, Minimum Window |
| Fast & Slow Pointers | Linked List Cycle, Reorder List |
| DFS/BFS | Number of Islands, Clone Graph |
| Binary Search | Classic, Rotated Array, Median |
| DP | Climbing Stairs, Coin Change, LIS |
| Backtracking | Subsets, Permutations, N-Queens |
| Heap | Kth Largest, Merge k Lists |

---

## Study Schedule Suggestion

| Week | Focus | Problems |
|------|-------|----------|
| 1 | Arrays & Strings | 10 |
| 2 | Linked Lists + Trees & Graphs | 15 |
| 3 | Sorting & Searching | 10 |
| 4 | Dynamic Programming | 10 |
| 5 | Backtracking | 10 |
| 6 | Design + Greedy | 15 |
| 7+ | Review & Mixed Practice | All |

---

## Complexity Cheat Sheet

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Array access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Subsets |
| O(n!) | Factorial | Permutations |

---

## Tips for Success

1. **Understand before memorizing** - Focus on patterns, not code
2. **Practice daily** - 2-3 problems per day
3. **Time yourself** - Simulate interview conditions
4. **Explain out loud** - Practice verbalizing your approach
5. **Review solutions** - Learn from multiple approaches
6. **Track progress** - Note which patterns need more work

---

Good luck with your interview preparation! 🚀
