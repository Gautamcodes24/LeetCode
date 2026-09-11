class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()
        visited = [False] * len(digits)
        def dfs(arr):
            # Base case: We have formed a 3-digit number
            if len(arr) == 3:
                # Ensure no leading zero and the number is even
                if arr[0] != 0 and arr[-1] % 2 == 0:
                    ans.add(tuple(arr))
                return
            # Loop through all digits to generate permutations, not just combinations
            for i in range(len(digits)):
                if not visited[i]:
                    visited[i] = True
                    arr.append(digits[i])
                    dfs(arr)
                    # Backtrack
                    arr.pop()
                    visited[i] = False

        dfs([])
        return len(ans) 