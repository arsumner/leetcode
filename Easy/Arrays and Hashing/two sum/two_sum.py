class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, val in enumerate(nums):
            difference = target - val
            if difference in seen:
                return [min(i, seen[difference]), max(i, seen[difference])]
            seen[val] = i

test = Solution()
nums = [1,2,3,4]
target = 6
print(test.twoSum(nums,target))