class Solution:
    def sortDigit(self, num: int) -> int:
        res = 0
        temp = num
        while temp != 0:
            rem = temp % 10
            res += rem
            temp = temp // 10
        return res

    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        indexed_nums = []
        for i, num in enumerate(nums):
            indexed_nums.append((self.sortDigit(num), num, i))
        indexed_nums.sort(key=lambda x: (x[0], x[1]))
        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i] or indexed_nums[i][2] == i:
                continue
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = indexed_nums[curr][2]
                cycle_size += 1  
            if cycle_size > 1:
                swaps += (cycle_size - 1)
        return swaps