class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(start_num, current_path, current_sum):
            if len(current_path) == k and current_sum == n:
                res.append(list(current_path))
                return
            
            if len(current_path) == k or current_sum > n:
                return
                
            for i in range(start_num, 10):
                current_path.append(i)
                backtrack(i + 1, current_path, current_sum + i)
                current_path.pop() # Backtrack step
                
        backtrack(1, [], 0)
        return res