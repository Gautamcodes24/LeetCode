class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preMul = [1] * len(nums)
        preFix = 1
        for indx in range(len(nums)):
            preMul[indx] = preFix
            preFix *= nums[indx]
        postFix = 1
        for indx in range(len(nums)-1 , -1 , -1):
            preMul[indx] *= postFix
            postFix *= nums[indx]
        return preMul
        