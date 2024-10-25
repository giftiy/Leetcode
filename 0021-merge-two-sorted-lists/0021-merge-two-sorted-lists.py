from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        # Merge the two lists
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach any remaining nodes
        tail.next = list1 if list1 else list2
        
        return dummy.next

# Test the solution
if __name__ == "__main__":
    # Create sample lists for testing
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)

    # Print merged list
    current = merged_list
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
