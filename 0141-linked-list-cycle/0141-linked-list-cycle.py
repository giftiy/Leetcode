# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Initialize two pointers, slow and fast
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next         # move slow pointer by 1 step
            fast = fast.next.next    # move fast pointer by 2 steps
            
            if slow == fast:  # cycle detected
                return True
        
        # If fast pointer reaches the end, no cycle exists
        return False
