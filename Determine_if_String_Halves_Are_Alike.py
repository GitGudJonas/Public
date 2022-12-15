############ Aestheticc enter #########
import numpy as np
#######################################
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        b=(s[len(s)//2:]).lower()
        a=(s[:-len(s)//2]).lower()
        ca=a.count('a')+a.count('e')+a.count('i')+a.count('o')+a.count('u')
        cb=b.count('a')+b.count('e')+b.count('i')+b.count('o')+b.count('u')
        return ca==cb
            
    
print(Solution().halvesAreAlike(s = "book")) #Output:  T
print(Solution().halvesAreAlike(s = "textbook")) #Output: F
