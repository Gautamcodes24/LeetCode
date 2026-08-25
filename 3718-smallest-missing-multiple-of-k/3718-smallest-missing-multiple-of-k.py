class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        mul = k
        while k in nums:
            print(k)
            k += mul
        return k
        