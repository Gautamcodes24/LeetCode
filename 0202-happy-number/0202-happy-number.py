# class Solution:
#     def isHappy(self, n: int) -> bool:
#         if n <= 10:
#             return False
#         while n > 1:
#             n = sum([int(num) ** 2 for num in str(n)])
#         return n == 1
class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_of_squares(num):
            total = 0
            while num > 0:
                digit = num % 10       # extract last digit
                total += digit ** 2    # square it
                num //= 10             # remove last digit
            return total

        slow = n
        fast = n

        while True:
            slow = sum_of_squares(slow)           # 1 step
            fast = sum_of_squares(sum_of_squares(fast))  # 2 steps

            if fast == 1:
                return True   # escaped to 1 → happy 🎉

            if slow == fast:
                return False  # caught in a cycle → not happy ❌