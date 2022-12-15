############ Aestheticc enter #########
from numpy import unique
import time
#######################################
class Solution:
    def uniqueOccurrences(self, arr:list[int]) -> bool:
        UniqueValues, counts=unique(arr, return_counts=True)
        l=len(UniqueValues)
        k=len(unique(counts))
        return l==k
start = time.time()
print(Solution().uniqueOccurrences(arr = [1,2,2,1,1,3])) #T
print(Solution().uniqueOccurrences(arr = [1,2])) #F
print(Solution().uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0])) #T
end = time.time()
print("time", end - start, "s")
