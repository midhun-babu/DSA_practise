"""
LeetCode #155: Min Stack
Category: Design Problems
Difficulty: Medium

Problem:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

LEARNING FOCUS:
- Tracking min with each element
- Auxiliary stack approach
"""


class MinStack:
    """
    Stack with O(1) min operation.
    
    THE INTUITION:
    Store (value, current_min) for each element.
    current_min is the minimum of all elements below and including this one.
    
    Time: O(1) for all operations
    Space: O(n)
    """
    
    def __init__(self):
        self.stack = []  # Each element: (value, current_min)
    
    def push(self, val: int) -> None:
        """Push value onto stack."""
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))
    
    def pop(self) -> None:
        """Remove top element."""
        self.stack.pop()
    
    def top(self) -> int:
        """Get top element."""
        return self.stack[-1][0]
    
    def getMin(self) -> int:
        """Get minimum element."""
        return self.stack[-1][1]


# ============== TEST ==============
if __name__ == "__main__":
    min_stack = MinStack()
    
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(f"getMin(): {min_stack.getMin()}")  # returns -3
    
    min_stack.pop()
    print(f"top(): {min_stack.top()}")        # returns 0
    print(f"getMin(): {min_stack.getMin()}")  # returns -2
