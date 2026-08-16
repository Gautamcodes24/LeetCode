class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        lmax = height[0]
        rmax = height[-1]
        water_cap = 0
        while l < r:
            if lmax > rmax:
                r -= 1
                rmax = max(height[r],rmax)
                water_cap += rmax - height[r]  
            else:
                l += 1
                lmax = max(height[l],lmax)
                water_cap += lmax - height[l]  
        return water_cap


