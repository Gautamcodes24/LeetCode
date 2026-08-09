class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for indx , temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                pop = stack.pop()
                ans[pop] = indx - pop
            stack.append(indx)
        return ans
