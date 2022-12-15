############ Aestheticc enter #########
import numpy as np
#######################################
class Solution:
    def twoSum(self, nums:list[int], target: int) -> list[int]:
        
##        for i in range(0,len(nums)//2+1):
##            for j in range(i+1,len(nums)):
##                
##                if nums[i]+nums[j]==target:
##                    
##                    x=[]
##                    x.append(i)
##                    x.append(j)
##                    
##                    return (x)
        #####################attempt two
##        move=[]
##        for i in range(1,len(nums)):
##            move=np.append([0]*i,nums)
##            nums=np.array(nums)
##            ad=np.sum([nums,move[:-i]],axis=0)
##            loc=np.argwhere(ad==target)
##            numstarget=(target-nums[loc])
##            if len(nums==1):
##                locnum=np.nonzero(nums==numstarget)
##                
##
##            else:
##                flipnums=np.flip(nums)
##                locnum=np.nonzero(flipnums==numstarget)
##            if loc.size>0:
##                break
##        if locnum[1][0]!=loc[0][0]:
##            return [locnum[1][0],loc[0][0]]
##        else:
##            return [locnum[1][1],loc[0][0]]
#################### attempt three
        
        rev=nums.copy()
        nums.reverse()

        for i in range(len(nums)):
##            
            sub=target-nums[i]
##            print(rev)
##            print(nums)
            
           
            try:
                nums.remove(sub)
                #ind=rev.index(sub)
            except ValueError:
                
                continue
            print(nums)
##            print(target)
##            print(sub)
##            print(nums[i])
##            print(rev.index(sub))
##            print(rev.index(nums[i]))

##            if nums.index(sub)>-1:
##                break
##            ind=nums.index(sub)
##        if ind!=i:
##            return [ind,i]
##        else:
##            return [ind,i]
print(Solution().twoSum(nums=[2, 7, 11, 15], target=9)) #Output: [0,1]
print(Solution().twoSum(nums=[2, 7, 11, 15], target=18)) #Output: [1,2]
print(Solution().twoSum(nums=[2, 7, 11, 15], target=22)) #Output: [1,3]
print(Solution().twoSum(nums=[2,4,11,3], target=6)) #Output: [0,1]
print(Solution().twoSum(nums=[0, 7, 11, 0], target=0)) #Output: [0,3]
print(Solution().twoSum(nums = [3,2,4], target = 6)) #Output: [1,2]
print(Solution().twoSum(nums = [3,3], target = 6)) #Output: [0,1]
