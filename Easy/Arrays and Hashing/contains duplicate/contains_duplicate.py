class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        counts = {n: 0 for n in nums}
        for i in nums:
            if counts[i] == 1:
                return True
            else:
                counts[i] += 1
        return False