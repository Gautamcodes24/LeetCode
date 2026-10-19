class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        # --------------Method 1----------------
        # lst=[]
        # for indx,num in enumerate(nums):
        #     if num == target:
        #         lst.append(indx)
        # return lst
        # --------------Method 2----------------
        return [indx for indx,num in enumerate(nums) if num == target]
