class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lg = 0
        l = 0
        sub = set()
        for r in range(len(s)):
            c = s[r]
            while c in sub:
                sub.remove(s[l])
                l += 1
            sub.add(c)
            lg = max(lg , r-l+1)
        return lg