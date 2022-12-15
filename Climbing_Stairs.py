############ Aestheticc enter #########
#import numpy as np
#from collections import Counter

#######################################
##Definition for a binary tree node.
class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=1,1
        for i in range(0,n):
            a,b=a+b,a
        return b

    
################################################################
##print(Solution().leafSimilar(root1 = [3,5,1,6,2,9,8,None,None,7,4], root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])) #Output: T
print(Solution().climbStairs(1)) #Output: F
print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
      
print(Solution().climbStairs(4))
print(Solution().climbStairs(5))
print(Solution().climbStairs(6))
##root = TreeNode(1, TreeNode(2), TreeNode(20, TreeNode(15), TreeNode(7)))

