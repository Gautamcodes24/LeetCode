class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        kad = float('-inf')
        run = 0
        if len(nums) == 1:
            return nums[0]
        for r in range(len(nums)):
            num = nums[r]
            run += num
            kad = max(kad , run)
            if run < 0:
                run = 0
        return kad if kad != float('-inf') else 0
             

        