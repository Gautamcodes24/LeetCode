class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr = 0
        seen = {0:1}
        for r in range(len(nums)):
            curr += nums[r]
            need = curr - k
            if need in seen:
                count += seen[need]
            seen[curr] = seen.get(curr,0) +1
        return count

        