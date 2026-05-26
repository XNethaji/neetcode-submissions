# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 0
        curr = cur = head 

        while cur:
            count += 1
            cur = cur.next
            
        if count == n:
            return head.next
        
        j = (count - n) 
        count1 = 1

        while curr and curr.next:
            if count1 == j:
                curr.next = curr.next.next
                count1 +=1
            else:
                curr = curr.next
                count1 +=1
        return head



        