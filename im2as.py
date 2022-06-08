import cv2 as cv
import numpy as np
word="ra"
#levels=len(word)-1
levels=1
def levelsValues(x):
    t=[]
    for i in range(0,256,int(x)):
        t.append(i)
    return t
def diff(val,list):
    list2=[]
    for i in range(len(list)):
        list2.append(abs(list[i]-val))
    index=0
    for i in range(len(list2)-1):
        if list2[i]>list2[i+1]:
            index = i+1
    return index


img=cv.imread("rabbit1.jpg")
img=cv.resize(img,[1000,1000])
#convert to gray scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imwrite("graypic.tiff",gray)
print("wrote pic before scale")
W,H = gray.shape
#sort by frequency
sorted=gray.flat
sorted=np.sort(sorted,-1,'quicksort')
unique_elements, frequency = np.unique(gray, return_counts=True)
sorted_indexes = np.argsort(frequency)[::-1]
sorted_by_freq = unique_elements[sorted_indexes]

#filter by levels demand

main_level=sorted_by_freq[0]
x=255/levels
levelsvalues=levelsValues(x)
#change image by filter
for i in range(H):
    for j in range(W):
        gray[j,i]=levelsvalues[diff(gray[j,i],levelsvalues)]
        #gray[j,i]=diff(gray[j,i],levelsvalues)
cv.imwrite("grayafterlevelscale.tiff",gray)
print("wrote pic after scale")
gray=gray.flat
#write to file 
"""
f = open("restxt.txt", "w")
for i in range(H):
    for j in range(W):
        f.write(word[int(gray[j,i])])
    f.write('\n')
f.close()
"""
if 0:
    f = open("restxt", "w")
    for i in range(len(gray)):
        if i%H==0:
            f.write('\n')
        f.write(word[int(gray[i])])
        
    f.close()
