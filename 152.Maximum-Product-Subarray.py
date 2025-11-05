def maxProduct(nums):
    best, maxn, minn = (nums[0],)*3
    
    for num in nums[1:]:
        vals = (num, maxn*num, minn*num)
        maxn, minn = max(vals), min(vals)
        best = max(best, maxn)       
        
    return best

test = [-1,4,-4, 5,-2,-1,-1,-2,-3]
print(maxProduct(test))
print('\n')
print(maxProduct([-2,3,-4]))

