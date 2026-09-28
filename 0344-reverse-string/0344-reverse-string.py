class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        def reverse(l):
            n = len(s)
            if l >= (n // 2):
                return
            s[l] , s[n-l - 1] = s[n-l-1] , s[l]
            reverse(l+1)
        reverse(0)
        
        