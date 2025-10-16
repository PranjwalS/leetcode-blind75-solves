def rob(nums):
    if len(nums)<2:
        return max(nums)
    
    max_loot=nums.copy()
    max_loot[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        max_loot[i] = max(max_loot[i-1], max_loot[i-2]+nums[i])
    
        
    return max_loot[-1]


        
    
    

print(rob([2,1,1,2]))
print(rob([1,2,3,4,5,6]))
print(rob([2,1,3,10,3]))
print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))