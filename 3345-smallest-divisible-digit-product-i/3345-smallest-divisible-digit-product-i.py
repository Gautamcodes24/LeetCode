class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def mul(num):
            ans = 1
            while num > 0:
                ans *= num % 10
                num //= 10
            return ans
        while True:
            nm = mul(n)
            if nm % t == 0:
                return n
            else:
                n += 1