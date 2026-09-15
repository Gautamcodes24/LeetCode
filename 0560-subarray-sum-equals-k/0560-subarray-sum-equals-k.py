class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0:1}
        ans = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            need = curr_sum - k
            if need in hm:
                ans += hm.get(need)
            hm[curr_sum] = hm.get(curr_sum,0)+1
        return ans

            