class Solution:
    def isPrefix(self,word,s):
        ps = ""
        for wc in s:
            ps += wc
            if len(word) == len(ps) and ps == word:
                return True
        return False
    def countPrefixes(self, words: list[str], s: str) -> int:
        count = 0
        for word in words:
            if self.isPrefix(word,s):
                print(word)
                count += 1
        return count

        