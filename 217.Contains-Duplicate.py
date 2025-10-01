class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))

    

sol = Solution()
nums = [3,1,1]
nums2 = [1,2,3,4]
print(sol.containsDuplicate(nums))
print(sol.containsDuplicate(nums2))