class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for indx , num in enumerate(nums):
            if target - num in seen:
                return [indx , seen[target - num]]
            seen[num] = indx
        