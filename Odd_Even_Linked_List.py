############ Aestheticc enter #########
#import numpy as np
#from collections import Counter

#######################################
##Definition for singly-linked list. Expanded for python at home
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"
def list_to_LL(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))
##############################################################        
class Solution:
    def oddEvenList(self, head:ListNode) -> ListNode:
        if not head:
            return head

        odd_head = head
        even_head_copy = even_head = head.next

        while odd_head and even_head and even_head.next:
            odd_head.next = even_head.next
            odd_head = odd_head.next

            even_head.next = odd_head.next
            even_head = even_head.next

        odd_head.next = even_head_copy
        
        return head
############# test cases ########
t1 = list_to_LL([1,2,3,4,5])
#t2 = list_to_LL([2,1,3,5,6,4,7]) 
############ outputs ############
print(Solution().oddEvenList(t1)) #Output: [1,3,5,2,4]
#print(Solution().oddEvenList(t2)) #Output: [2,3,6,7,1,5,4]
