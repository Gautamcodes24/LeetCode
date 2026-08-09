class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = nums[0]
        cur_max, cur_min = 1, 1

        for num in nums:
            # If num is negative, swapping cur_max and cur_min 
            # handles the sign inversion cleanly.
            if num < 0:
                cur_max, cur_min = cur_min, cur_max

            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)

            res = max(res, cur_max)

        return res