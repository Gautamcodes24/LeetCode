class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # for indx , f in enumerate(flowerbed):
        for indx in range(len(flowerbed)):
            if flowerbed[indx] == 0:
                left_side = (indx == 0) or (flowerbed[indx-1] == 0)
                right_side = (indx == len(flowerbed)-1) or (flowerbed[indx+1] == 0)
                if left_side and right_side:
                    flowerbed[indx] = 1
                    n -= 1
                # print(flowerbed)
                if n == 0:
                    return True
        return n <= 0