def canJump(nums):
    curr = 0
    index = 0
    while index<=curr:
        curr = max(curr, index+nums[index])
        if curr>=len(nums)-1:
            return True
        index+=1
    return False
        

nums = [2,3,1,1,4]
nums2 = [3,2,1,0,4]
print(canJump(nums)) #true
print(canJump(nums2)) #false