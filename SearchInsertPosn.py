def searchInsert(nums: list[int], target: int) -> int:
    l1=nums

    if target in nums:
        while(len(l1)!=0):
            mid=len(l1)//2
            if target>l1[mid]:
                l1=l1[mid+1:len(l1)]
            elif target<l1[mid]:
                l1=l1[0:mid]
            else:
                return(nums.index(l1[mid]))
    if target not in nums:
        while(len(l1)!=1):
            mid=len(l1)//2
            if target>l1[mid]:
                l1=l1[mid:len(l1)]
            elif target<l1[mid]:
                l1=l1[0:mid]
            else:
                return(mid)
        if target>l1[0]:
            return(nums.index(l1[0])+1)
        else:
            if (nums.index(l1[0])==0):
                return(0)
            else:
                return((nums.index(l1[0]))-1)

nums=[1,3,5]
target=5
index = searchInsert(nums,target)
print(index)