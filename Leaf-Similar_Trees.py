############ Aestheticc enter #########
#import numpy as np
#from collections import Counter

#######################################
##Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1:[TreeNode], root2:[TreeNode]) -> bool:
        def fn(node):
            return (fn(node.left) + fn(node.right) or [node.val]) if node else []

        return fn(root1) == fn(root2)
    
################################################################
##print(Solution().leafSimilar(root1 = [3,5,1,6,2,9,8,None,None,7,4], root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])) #Output: T
print(Solution().leafSimilar(root1 = TreeNode(1, TreeNode(2), TreeNode(3)), root2 = TreeNode(1, TreeNode(2), TreeNode(3)))) #Output: F
##root = TreeNode(1, TreeNode(2), TreeNode(20, TreeNode(15), TreeNode(7)))

