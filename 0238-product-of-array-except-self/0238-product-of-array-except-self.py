class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        preMul = [1] * len(nums)
        prefix = 1
        for indx in range(len(nums)):
            preMul[indx] = prefix
            prefix *= nums[indx]
        prefix = 1
        for indx in range(len(nums)-1 , -1 , -1):
            preMul[indx] *= prefix
            prefix *= nums[indx]
        return preMul

        