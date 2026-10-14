# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer1 = head
        pointer2 = head
        while pointer1 and pointer2 is not None:
            if pointer2.next and pointer2.next.next:
                pointer2 = pointer2.next.next
            else:
                return False
                
            pointer1= pointer1.next
            if pointer2 == pointer1:
                return True
        else:
            return False
        