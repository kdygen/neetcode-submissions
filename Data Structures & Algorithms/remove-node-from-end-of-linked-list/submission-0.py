# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1. first reverse the list
# 2. move next while count < n
# 3. then asign the current.next to current.next.next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        current = head      #[1,2,3,4] 
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        if n == 1:
            prev = prev.next
        else:
            count = 1
            current1 = prev
            while count < n - 1:
                current1 = current1.next
                count += 1

            current1.next = current1.next.next

        current = prev
        prev = None
        
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        return prev