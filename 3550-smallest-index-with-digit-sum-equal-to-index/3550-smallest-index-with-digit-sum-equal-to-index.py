class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for indx , num in enumerate(nums):
            _sum = sum(int(n) for n in str(num))
            if _sum == indx:
                return indx
        return -1
        