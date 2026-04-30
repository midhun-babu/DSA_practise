"""
LeetCode #208: Implement Trie (Prefix Tree)
Category: Design Problems
Difficulty: Medium

Problem:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently
store and retrieve keys in a dataset of strings. There are various applications of this data structure,
such as autocomplete and spellchecker.

Implement the Trie class with insert, search, and startsWith operations.

LEARNING FOCUS:
- Tree-based string storage
- Prefix matching
- Node structure design
"""


class TrieNode:
    
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.is_end = False  # Marks end of a word


class Trie:
   
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """Insert word into trie."""
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end = True
    
    def search(self, word: str) -> bool:
        """Return True if word is in trie."""
        node = self._find_node(word)
        return node is not None and node.is_end
    
    def startsWith(self, prefix: str) -> bool:
        """Return True if any word starts with prefix."""
        return self._find_node(prefix) is not None
    
    def _find_node(self, word: str) -> TrieNode:
        """Find node corresponding to word, or None."""
        node = self.root
        
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        
        return node


# ============== TEST ==============
if __name__ == "__main__":
    trie = Trie()
    
    trie.insert("apple")
    print(f"search('apple'): {trie.search('apple')}")      # True
    print(f"search('app'): {trie.search('app')}")          # False
    print(f"startsWith('app'): {trie.startsWith('app')}")  # True
    
    trie.insert("app")
    print(f"search('app'): {trie.search('app')}")          # True
