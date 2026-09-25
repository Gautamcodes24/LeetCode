class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = [0 for _ in range(len(nums) * 2)]
        n = len(nums)
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[n+i] = nums[i]
        return ans
        