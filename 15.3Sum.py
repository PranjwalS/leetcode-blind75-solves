def threeSum(nums):
    output = []
    nums.sort()
    for i in range(len(nums)):
        if i>0 and nums[i] == nums[i-1]: continue
        j, k = i+1, len(nums)-1
        while j<k:
            sum = nums[i]+nums[j]+nums[k]
            if sum == 0:
                output.append([nums[i], nums[j], nums[k]])
                j, k = (j+1, k-1)
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
            elif sum < 0:
                j+=1
            else:
                k-=1
    return output

print(threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))
print(threeSum([0,0,0]))