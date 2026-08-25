class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(indx , arr , total):
            if total == target:
                res.append(arr.copy())
                return
            if total > target or indx == len(candidates):
                return
            arr.append(candidates[indx])
            dfs(indx , arr ,total+candidates[indx])
            arr.pop()
            dfs(indx+1 , arr ,total)
        dfs(0,[],0)
        return res

        