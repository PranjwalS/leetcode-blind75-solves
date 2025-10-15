def missingNumber(nums):
    # for i in range(len(nums)+1):
    #     if i not in nums:
    #         return i
    
    # return sum(range(len(nums)+1))-sum(nums)
    # lst = [i for i in range(len(nums)+1)]
    
    xor = 0
    for i in range(len(nums)):
        xor ^= i
        xor ^= nums[i]
    return xor^len(nums)


print(missingNumber([3,1,0]))
print(missingNumber([0,1]))
# assert (missingNumber([9,6,4,2,3,5,7,0,1])) == 8
# assert (missingNumber([3,0,1])) == 2
# assert (missingNumber([0,1])) == 2
# print("all passed")