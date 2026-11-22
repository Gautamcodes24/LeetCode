class Solution:
    def checkString(self, s: str) -> bool:
        maps={}
        for i , c in enumerate(s):
            if c not in maps:
                maps[c] = []
            maps[c].append(i)
        if len(maps) == 1:
            return True
        max_p_a = max(maps.get('a'))
        min_p_b = min(maps['b'])
        return max_p_a < min_p_b
            
        