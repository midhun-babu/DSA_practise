"""
LeetCode #146: LRU Cache
Category: Design Problems
Difficulty: Medium

Problem:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class with get and put operations in O(1) time.

LEARNING FOCUS:
- Hash Map + Doubly Linked List combination
- O(1) operations design
- Cache eviction policy
"""


class ListNode:
    """Doubly linked list node."""
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    LRU Cache using Hash Map + Doubly Linked List.
    
    THE INTUITION:
    - Hash Map: O(1) lookup by key
    - Doubly Linked List: O(1) removal and insertion at both ends
    
    Most recently used items are at front (after head).
    Least recently used items are at back (before tail).
    
    Time: O(1) for both get and put
    Space: O(capacity)
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node
        
        # Dummy head and tail
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: ListNode):
        """Remove node from list."""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def _add_to_front(self, node: ListNode):
        """Add node right after head."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _move_to_front(self, node: ListNode):
        """Move existing node to front."""
        self._remove(node)
        self._add_to_front(node)
    
    def _pop_tail(self) -> ListNode:
        """Remove and return node before tail."""
        node = self.tail.prev
        self._remove(node)
        return node
    
    def get(self, key: int) -> int:
        """Get value and mark as recently used."""
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_front(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        """Insert or update key-value pair."""
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
            
            if len(self.cache) > self.capacity:
                lru = self._pop_tail()
                del self.cache[lru.key]


# ============== TEST ==============
if __name__ == "__main__":
    cache = LRUCache(2)
    
    cache.put(1, 1)  # cache: {1=1}
    cache.put(2, 2)  # cache: {1=1, 2=2}
    print(f"get(1): {cache.get(1)}")  # returns 1
    
    cache.put(3, 3)  # evicts key 2, cache: {1=1, 3=3}
    print(f"get(2): {cache.get(2)}")  # returns -1
    
    cache.put(4, 4)  # evicts key 1, cache: {3=3, 4=4}
    print(f"get(1): {cache.get(1)}")  # returns -1
    print(f"get(3): {cache.get(3)}")  # returns 3
    print(f"get(4): {cache.get(4)}")  # returns 4
