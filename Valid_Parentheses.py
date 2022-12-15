############ Aestheticc enter #########
#import numpy as np
#from collections import Counter

#######################################
class Solution:
    def isValid(self, s: str) -> bool:
        while (s.find("()")!=-1 or s.find("{}")!=-1 or s.find("[]")!=-1):
            s=s.replace("{}","")
            s=s.replace("[]","")
            s=s.replace("()","")
        return s==""
    
################################################################
print(Solution().isValid(s = "()")) #Output: T
print(Solution().isValid(s = "([[[]]][])")) #Output: T
print(Solution().isValid(s = "([{]})")) #Output: F

