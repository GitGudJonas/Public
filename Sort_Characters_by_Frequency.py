############ Aestheticc enter #########
#import numpy as np
from collections import Counter

#######################################
class Solution:
    def frequencySort(self, s: str) -> str:
        u = Counter(s).most_common()
        w=""
        for letter,count in u:
            w+=(letter*count)
            
        return w

############ Solution sets ############
print(Solution().frequencySort(s = "tree")) #Output: eert
print(Solution().frequencySort(s = "cccaaa")) #Output: "aaaccc"
print(Solution().frequencySort(s = "Aabb")) #Output: "bbAa"
##print(Solution().frequencySort(nums=[2,4,11,3], target=6)) #Output: [0,1]
##print(Solution().frequencySort(nums=[0, 7, 11, 0], target=0)) #Output: [0,3]
##print(Solution().frequencySort(nums = [3,2,4], target = 6)) #Output: [1,2]
##print(Solution().frequencySort(nums = [3,3], target = 6)) #Output: [0,1]
