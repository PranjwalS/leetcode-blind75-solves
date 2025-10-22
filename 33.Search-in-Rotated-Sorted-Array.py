def search(nums, target):
    low, high = 0, len(nums)-1
    while low<= high:
        middle = (low+high)//2
        if nums[middle]==target:
            return middle
        
        if nums[low] <= nums[middle]:
            if target>=nums[low] and target<=nums[middle]:
                high = middle-1
            else:
                low = middle+1
        
        else:
            if target>=nums[middle] and target<=nums[high]:
                low = middle+1
            else:
                high=middle-1
    return -1
                


print(search([4,5,6,7,0,1,2], 0))
print(search([4,5,6,7,0,1,2], 3))