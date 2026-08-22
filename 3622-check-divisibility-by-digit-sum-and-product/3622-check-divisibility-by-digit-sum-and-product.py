class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sm = 0
        pr = 1
        num = n
        while n != 0:
            curr_d = n % 10
            sm += curr_d
            pr *= curr_d
            n //= 10
        return num % (sm + pr) == 0
        