#Uniform Experiments
import numpy as np
import time
import matplotlib.pyplot as plt
from collections import Counter
#aesthetic enter
def motion(n):
    global mean, median, count
    s = np.random.uniform(0,1,n) #samples
    mean=np.mean(s)
    median=np.median(s)
    count=(s>mean).sum()
l=int(input('Length? '))
t=int(input('Times? '))
start = time.time()
meanlist=[]
medianlist=[]
counter=[]
for i in range(t):
    motion(l)
    meanlist=np.append(meanlist,mean)
    medianlist=np.append(medianlist,median)
    counter=np.append(counter,count)
print(meanlist)
print(medianlist)
skew=meanlist-medianlist
print(skew)
print(counter)
print(len(np.unique(counter)))
print(Counter(counter))
np.savetxt('UniN.txt', np.transpose([meanlist,medianlist,skew,counter]),fmt='%1.6f,%1.6f,%1.6f,%i')
#plotcode

plt.figure()


# mean
plt.subplot(221)
plt.hist(meanlist,bins=50)
plt.title('Mean')
#median
plt.subplot(222)
plt.hist(medianlist,bins=50)
plt.title('Median')
#Skew
plt.subplot(223)
plt.hist(skew,bins=50)
plt.title('Skew')
#Count
plt.subplot(224)
plt.hist(counter, bins=len(np.unique(counter)))
plt.title('counter>avg')

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

end = time.time()
print("program ran in", end - start, "seconds")
plt.show()
