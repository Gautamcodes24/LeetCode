class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        longest = 0
        l = 0
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r],0)+1
            while (r-l+1) - max(hm.values()) > k:
                hm[s[l]] = hm.get(s[l],0) - 1
                if hm[s[l]] == 0:
                    del hm[s[l]]
                l += 1
            longest = max(longest , r-l+1)
        return longest