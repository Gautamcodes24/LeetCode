class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_cap = 0
        l = 0
        r = len(height) - 1
        while l < r:
            if height[l] < height[r]:
                width = r - l
                # h = min(height[l],)
                area = height[l] * width
                max_cap = max(max_cap , area)
                l += 1
            else:
                width = r - l
                # h = min(height[l],)
                area = height[r] * width
                max_cap = max(max_cap , area)
                r -= 1
        return max_cap
        