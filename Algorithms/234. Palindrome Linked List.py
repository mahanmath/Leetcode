# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if(not head): return True
        curr = head
        l = [head.val]
        while(curr.next != None):
            curr=curr.next
            l.append(curr.val)
        return(l == l[::-1])        
