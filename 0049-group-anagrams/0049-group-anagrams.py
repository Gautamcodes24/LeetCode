class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = []
        hmap = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in hmap:
                hmap[sorted_word] = []
            hmap[sorted_word].append(word)
        return [val for val in hmap.values()]


        