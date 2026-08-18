class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        def helper(indx, currSum):
            if indx == len(nums):
                return
            currSum += nums[indx]
            ans.append(currSum)
            helper(indx+1 , currSum)
        helper(0,0)
        return ans
        