class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero , two , curr = 0 , len(nums) - 1 , 0
        while curr <= two:
            if nums[curr] == 0:
                nums[zero] , nums[curr] = nums[curr] , nums[zero]
                zero += 1
                curr += 1
            elif nums[curr] == 2:
                nums[two] , nums[curr] = nums[curr] , nums[two]
                two -= 1
            else:
                curr += 1