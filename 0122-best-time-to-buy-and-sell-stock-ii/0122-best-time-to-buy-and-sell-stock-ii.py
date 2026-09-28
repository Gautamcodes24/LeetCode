class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        max_p = 0
        for indx , num in enumerate(prices):
            stock = [num]
            r = indx + 1
            while r < n and stock[-1] < prices[indx + 1]:
                stock.append(prices[r])
                r += 1
            if len(stock) > 1:
                max_p += stock[-1] - stock[0]
        return max_p
        