def maxSubArray(nums):
    current = 0
    best = max(nums)
    
    for i in range(len(nums)):
        current = max(nums[i], current+nums[i])
        best = max(current, best)

    return best



print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

print(maxSubArray([5,4,-1,7,8]))

print(maxSubArray([1]))