class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n *= -1
        def calpow(x,pow):
            nonlocal ans
            if pow == 0:
                return
            if pow % 2 == 1:
                ans *= x
            pow = pow // 2
            return calpow(x * x , pow)
        calpow(x,n)
        return ans

            


        