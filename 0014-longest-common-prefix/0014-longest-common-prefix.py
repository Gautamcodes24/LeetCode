class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        lng = ""
        strs.sort()
        print(strs)
        for i , c in enumerate(strs[0]):
            if all(word[i] == c for word in strs):
                lng += c
            else:
                return lng
        return lng
        