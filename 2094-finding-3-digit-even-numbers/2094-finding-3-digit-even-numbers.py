
from collections import Counter
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        digit_count = Counter(digits)
        for combo in range(100,999,2):
            str_digit = str(combo)
            if all(str_digit.count(d) <= digit_count[int(d)] for d in str_digit):
                ans.append(int(str_digit))
        return ans

            