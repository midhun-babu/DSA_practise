"""
LeetCode #622: Design Circular Queue
Category: Design Problems
Difficulty: Medium

Problem:
Design your implementation of the circular queue.
The circular queue is a linear data structure in which the operations are performed
based on FIFO (First In First Out) principle, and the last position is connected back
to the first position to make a circle. It is also called "Ring Buffer".

LEARNING FOCUS:
- Circular array implementation
- Front and rear pointers
- Full vs empty conditions
"""


class MyCircularQueue:
    
    
    def __init__(self, k: int):
        self.capacity = k
        self.queue = [0] * k
        self.head = -1  # Points to front element
        self.tail = -1  # Points to last element
        self.size = 0
    
    def enQueue(self, value: int) -> bool:
        """Insert element at rear."""
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.head = 0
        
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = value
        self.size += 1
        return True
    
    def deQueue(self) -> bool:
        """Delete element from front."""
        if self.isEmpty():
            return False
        
        if self.head == self.tail:
            # Last element
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity
        
        self.size -= 1
        return True
    
    def Front(self) -> int:
        """Get front element."""
        if self.isEmpty():
            return -1
        return self.queue[self.head]
    
    def Rear(self) -> int:
        """Get rear element."""
        if self.isEmpty():
            return -1
        return self.queue[self.tail]
    
    def isEmpty(self) -> bool:
        """Check if queue is empty."""
        return self.size == 0
    
    def isFull(self) -> bool:
        """Check if queue is full."""
        return self.size == self.capacity


# ============== TEST ==============
if __name__ == "__main__":
    cq = MyCircularQueue(3)
    
    print(f"enQueue(1): {cq.enQueue(1)}")  # True
    print(f"enQueue(2): {cq.enQueue(2)}")  # True
    print(f"enQueue(3): {cq.enQueue(3)}")  # True
    print(f"enQueue(4): {cq.enQueue(4)}")  # False (full)
    
    print(f"Rear(): {cq.Rear()}")          # 3
    print(f"isFull(): {cq.isFull()}")      # True
    
    print(f"deQueue(): {cq.deQueue()}")    # True
    print(f"enQueue(4): {cq.enQueue(4)}")  # True
    print(f"Rear(): {cq.Rear()}")          # 4
