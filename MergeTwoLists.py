nums1= [1,2,3,0,0,0]
nums2= [2,5,6]
m=3
n=3
if (n>0):
    for i in nums2:
        nums1.append(i)
nums1.sort()
for i in nums1:
    if (i==0):
        nums1.remove(i)
nums1.remove(0)
print(nums1)