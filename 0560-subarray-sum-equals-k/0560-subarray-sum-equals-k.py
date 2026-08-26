class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0:1}
        count = 0
        running_sum = 0
        for num in nums:
            running_sum += num 
            need = running_sum - k
            if need in hm:
                count += hm.get(need)
            hm[running_sum] = hm.get(running_sum,0)+1
        return count


        