class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        count = 0
        num = set(nums)
        for nm in num:
            if nm - 1 not in num:
                start = nm
                length = 1
                while start + 1 in num:
                    start += 1
                    length += 1
                count = max(count , length)
        return count