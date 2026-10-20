class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_p = 0
        l = 0
        for p in range(1,len(prices)):
            if prices[l] > prices[p]:
                l = p
            else:
                max_p = max(max_p , prices[p] - prices[l])
        return max_p