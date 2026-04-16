"""
LeetCode #706: Design HashMap
Category: Design Problems
Difficulty: Easy

Problem:
Design a HashMap without using any built-in hash table libraries.
Implement the MyHashMap class with put, get, and remove operations.

LEARNING FOCUS:
- Hash function design
- Collision handling (chaining)
- Dynamic resizing concept
"""


class MyHashMap:
   
    
    def __init__(self):
        self.size = 1000 
        self.buckets = [[] for _ in range(self.size)]
    
    def _hash(self, key: int) -> int:
        
        return key % self.size
    
    def put(self, key: int, value: int) -> None:
   
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Check if key exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update
                return
        
        # Key doesn't exist, add new
        bucket.append((key, value))
    
    def get(self, key: int) -> int:
        """Get value for key, return -1 if not found."""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return -1
    
    def remove(self, key: int) -> None:
        """Remove key-value pair if exists."""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return


# ============== TEST ==============
if __name__ == "__main__":
    hash_map = MyHashMap()
    
    hash_map.put(1, 1)
    hash_map.put(2, 2)
    print(f"get(1): {hash_map.get(1)}")    # returns 1
    print(f"get(3): {hash_map.get(3)}")    # returns -1
    
    hash_map.put(2, 1)  # update
    print(f"get(2): {hash_map.get(2)}")    # returns 1
    
    hash_map.remove(2)
    print(f"get(2): {hash_map.get(2)}")    # returns -1
