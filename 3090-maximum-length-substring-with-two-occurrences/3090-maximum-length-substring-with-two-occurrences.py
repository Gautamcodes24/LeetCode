class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        lng = 0
        hm = {}
        l = 0
        for r in range(len(s)):
            c = s[r]
            hm[c] = hm.get(c,0)+1
            while hm[c] > 2:
                hm[s[l]] = hm.get(s[l],0) - 1
                if hm.get(s[l],0) == 0:
                    del hm[s[l]]
                l += 1
            lng = max(lng , r-l+1)
        return lng