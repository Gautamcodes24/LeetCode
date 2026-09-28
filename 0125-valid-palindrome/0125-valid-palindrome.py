class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = "".join(c.lower() for c in s if 'a' <= c.lower() <= 'z' or c.isdigit())
        print(char)
        l = 0
        r = len(char) - 1
        while l < r:
            if char[l] != char[r]:
                return False
            l += 1
            r -= 1
        return True
        