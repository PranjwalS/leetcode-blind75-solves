def lengthOfLIS(nums):
    arr = [nums[0]]
    
    for i in range(1, len(nums)):
        print(arr)

        if nums[i]>arr[-1]:
            arr.append(nums[i])
            continue
        
        l, r = (0, len(arr))
        while l<r:
            mid = (l+r)//2
            if nums[i] > arr[mid]:
                l = mid+1
            else:
                r = mid          
        
        arr[l] = nums[i]
    return len(arr)

nums = [10,9,2,5,3,7,101,18]
nums2 = [0,1,0,3,2,3]
nums3 = [7,7,7,7,7,7,7]
print(lengthOfLIS(nums))

print(lengthOfLIS(nums2))

print(lengthOfLIS(nums3))


arr = [1,2,3,4,5]
val = (4, 1)
low, hi = 0, len(arr)
while low<hi:
    mid = (low+hi)//2
    if val[0] > arr[mid]:
        low = mid + 1
    else:
        hi = mid
arr.insert(low, val)
print(arr)