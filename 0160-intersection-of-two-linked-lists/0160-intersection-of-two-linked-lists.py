# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Initialize two pointers, pA and pB
        pA, pB = headA, headB
        
        # Traverse both lists
        while pA != pB:
            # Move each pointer to the next node, or to the head of the other list when reaching the end
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        # If there's no intersection, both pointers will be None.
        return pA

    