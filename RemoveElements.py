nums = [0,1,2,2,3,0,4,2]
val = 2
s=0
if (len(nums)>0):
    for j in range (0,2):
        for i in range (0,len(nums)):
            if nums[i] == val:
                nums.pop(i)
                s+=1
                nums.append("_")
    print(len(nums)-s)
else:
    print(0)