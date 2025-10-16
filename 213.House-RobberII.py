def rob(nums):
    if len(nums)<2:
        return max(nums)
    max_loot_first = nums[:-1]
    max_loot_last = nums[1:]    
    if len(max_loot_first)<=2 or len(max_loot_last)<=2:
        return max(max(max_loot_first), max(max_loot_last))
    
    max_loot_first[1] = max(nums[0], nums[1])
    max_loot_last[1] = max(nums[1], nums[2])
    
    for i in range(2, len(nums)-1):
        max_loot_last[i] = max(max_loot_last[i-1], max_loot_last[i-2]+nums[i+1])
        max_loot_first[i] = max(max_loot_first[i-1], max_loot_first[i-2]+nums[i])
    return max(max(max_loot_first), max(max_loot_last))

print(rob([1,3,1,3,100]))
print(rob([2,3,2,5,1]))
print(rob([2,1,3,10,3]))
print(rob([2,1,1,2]))
print(rob([2,7,9,3,1]))
print(rob([2,3,2]))
print(rob([1,2,3,1]))
print(rob([1,2,3]))