# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#[0, 1, 2, 3, 4, 5, 6]
#[0, 6, 1, 5, 2, 4, 3]

# 1. we want to keep the head position.
# 2. we need slow/fast
# 3. when slow reaches end we want starting from slow to reverse the list
# 4. merge them together
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        current = slow.next
        slow.next = None
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        list1 = head
        list2 = prev
        while list1 and list2:
            next1 = list1.next          #[0, 1, 2, 3, 4, 5, 6]
            next2 = list2.next          #[0,1,2,3]
                                        #[6,5,4]
            list1.next = list2
            list2.next = next1

            list1 = next1
            list2 = next2

        return list2