class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cand = None
        vote = 0
        for num in nums:
            if vote == 0:
                cand = num
            if cand == num:
                vote += 1
            else:
                vote -= 1
        return cand
        