############ Aestheticc enter #########
import numpy as np
#######################################
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return len(word1)==len(word2)
        else:
            w1=[]
            w2=[]
        for i in range(len(word1)):
            w1.append(word1[i])
            w2.append(word2[i])            
        v1,c1=np.unique(w1, return_counts=True)
        v2,c2=np.unique(w2, return_counts=True)
##        if np.count_nonzero(v1)!=np.count_nonzero(v2):
##            return np.count_nonzero(v1)==np.count_nonzero(v2)
##        else:
        c1.sort()
        c2.sort()
        return (np.array_equal(v1,v2) and np.array_equal(c1,c2))

############ Solution sets ############

print(Solution().closeStrings(word1 = "abc", word2 = "bca")) #Output: True
print(Solution().closeStrings(word1 = "a", word2 = "aa")) #Output: F
print(Solution().closeStrings(word1 = "cabbba", word2 = "abbccc")) #Output: T
print(Solution().closeStrings(word1 = "abbbzcf", word2 = "babzzcz")) #Output: F?
print(Solution().closeStrings(word1 = "uau", word2 = "ssx")) #Output: F?
