class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        ans = []
        threshold = len(nums) // 3
        if candidate1 is not None and nums.count(candidate1) > threshold:
            ans.append(candidate1)
        if candidate2 is not None and nums.count(candidate2) > threshold:
            ans.append(candidate2)
        return ans

        



        