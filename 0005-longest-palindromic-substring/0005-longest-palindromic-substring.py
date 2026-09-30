class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ''
        s_len = len(s)
        if s_len <= 1 or s == s[::-1]:
            return s
        for i in range(s_len):
            l = r = i
            while l >= 0 and r < s_len and s[l] == s[r]:
                if r - l + 1 > len(best):
                    best = s[l:r+1]
                l -= 1
                r += 1
            l , r = i , i + 1
            while l >= 0 and r < s_len and s[l] == s[r]:
                if r - l + 1 > len(best):
                    best = s[l:r+1]
                l -= 1
                r += 1
        return best
             