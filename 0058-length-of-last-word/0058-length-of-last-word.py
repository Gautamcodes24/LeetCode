class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        newList = []
        for strs in s.strip().split(" "):
            if strs == "":
                pass
            else:
                newList.append(strs)
        return len(newList.pop())