# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
##class Solution:
##    def addTwoNumbers(self, l1, l2) -> list:
##        x=[]
##        pad=abs(len(l1)-len(l2))
##        y=[0]*pad
##        if len(l1)-len(l2)>0:
##            list1=l1
##            list2=l2+y
##        else:
##            list1=l1+y
##            list2=l2
##        
##        
##        for i in range(0,max(len(l1),len(l2))):
##            if i>0 and (l1[i-1]+l2[i-1])>9:
##                x.append((l1[i]+l2[i]+1)%10)
##            else:
##                x.append((l1[i]+l2[i])%10)
##        return x
##import numpy as np
#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1:[ListNode], l2:[ListNode]) -> [ListNode]:

##        l1.reverse()
##        l2.reverse()
##        print(l1,l2)
        if len(l1)-len(l2)>0:
            
            l2=l2+[0]*(len(l1)-len(l2))
        else:
            l1=l1+[0]*(len(l2)-len(l1))
          
        x=0
        y=0
        for i in range(max(len(l1),len(l2))):
            x+=l1[i]*10**i
            y+=l2[i]*10**i
##        print(x+y)
        rem=[]
        for j in range(max(len(l1),len(l2))+1):
            rem.append((x+y)//10**j%(10))
            
##        print(rem)
        if rem[-1]==0:
            return rem[:-1]
        else:
            return rem
##        ad.reverse()
##        print(ad)
        
print(Solution().addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4])) #Output: [7,0,8]
print(Solution().addTwoNumbers(l1 = [0], l2 = [0])) #Output: [0]
print(Solution().addTwoNumbers(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9])) # [8,9,9,9,0,0,0,1]
print(Solution().addTwoNumbers(l2 = [9,9,9,9,9,9,9], l1 = [9,9,9,9])) # [8,9,9,9,0,0,0,1]

