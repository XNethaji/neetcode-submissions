# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None): 
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = curr1 = head
        length = 1
        if not head:
            return head

        while curr.next:
            length += 1
            curr = curr.next
        curr.next = head 
        k = k % length 
        val = length - k -1
        count = 0
        if k == length:
            return head

        while val != count:
            count += 1
            curr1 = curr1.next
        new = curr1.next
        curr1.next = None
        return new


    



        