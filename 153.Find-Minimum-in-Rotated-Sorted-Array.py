def findMin(nums):
    left, right = 0, len(nums)-1
    while left<right:
        middle = (left+right)//2
        if nums[middle]<nums[right]:
            right = middle
        else:
            left = middle+1
    return nums[right]
    
    


nums = [0,1,2,3,4,5]
print(findMin(nums))