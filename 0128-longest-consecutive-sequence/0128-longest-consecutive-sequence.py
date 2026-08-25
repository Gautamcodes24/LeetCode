class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        lng = 0
        for num in nums:
            if num - 1 not in nums:
                length = 1
                n = num
                while n + 1 in nums:
                    n += 1
                    length += 1
                lng = max(lng , length)
        return lng

        