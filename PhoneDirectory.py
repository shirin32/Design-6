"""
Design a phone directory that initially has maxNumbers empty slots 
that can store numbers. The directory should store numbers, 
check if a certain slot is empty or not, and empty a given slot.

Implement the PhoneDirectory class:

PhoneDirectory(int maxNumbers) Initializes the phone directory 
with the number of available slots maxNumbers.

int get() Provides a number that is not assigned to anyone. 
Returns -1 if no number is available.

bool check(int number) Returns true if the slot number is available 
and false otherwise.

void release(int number) Recycles or releases the slot number.
"""

# Time Complexity : O(1)
# Space Complexity : O(n)
# Did this code successfully run on VScode : Yes
# Any problem you faced while coding this : No

from collections import deque

class PhoneDirectory:
    
    def __init__(self, maxNumbers: int):
        
        self.q = deque()
        self.s = set()
        
        for i in range(maxNumbers):
            self.q.append(i)

    def get(self) -> int:
        
        if len(self.q) <= 0:
            return -1
        
        num = self.q.popleft()
        self.s.add(num)
        return num
        
    def check(self, number: int) -> bool:
        
        if number not in self.s:
            return True
        return False        

    def release(self, number: int) -> None:
        
        if number in self.s:
            self.s.remove(number)
            self.q.append(number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)