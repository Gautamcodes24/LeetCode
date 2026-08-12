class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hm = {}
        l = 0
        longest = 0
        for r in range(len(nums)):
            hm[nums[r]] = hm.get(nums[r],0)+1
            while hm[nums[r]] > k:
                hm[nums[l]] = hm.get(nums[l],0) - 1
                if hm.get(nums[l]) == 0:
                    del hm[nums[l]]
                l += 1
            longest = max(longest , r-l+1)
        return longest