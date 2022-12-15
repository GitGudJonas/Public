############ Aestheticc enter #########
#import numpy as np
#from collections import Counter

#######################################
class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        
        tobeat=1e5+1
        for i,value in enumerate(nums):
            leftdiv=i+1
            rightdiv=(len(nums)-i-1)
            left=sum(nums[0:i+1])
            right=sum(nums[i+1:])
            
            diff=abs(left//leftdiv-right//(rightdiv if rightdiv>0 else 1))
            if diff<tobeat:
                tobeat=diff
                output=i
            print(tobeat,diff,output)
        return output

#############GETS timeout error, probably due to appends and indexing ########
        
############ Solution sets ############
print(Solution().minimumAverageDifference(nums = [2,5,3,9,5,3])) #Output: 3
##print(Solution().minimumAverageDifference(nums = [0])) #Output: 0
##print(Solution().minimumAverageDifference(nums = [0,0,0,0,0])) #Output: 0

