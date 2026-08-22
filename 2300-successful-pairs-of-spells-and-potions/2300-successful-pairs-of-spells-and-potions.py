from bisect import bisect_left
import math

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        # Step 1: Sort the potions array
        potions.sort()
        m = len(potions)
        pairs = []
        
        # Step 2: For each spell, binary search the minimum valid potion
        for spell in spells:
            # Calculate minimum required potion strength (ceiling division)
            # min_potion = (success + spell - 1) // spell
            min_potion = math.ceil(success / spell)
            print(min_potion)
            # Find the first potion that meets or exceeds min_potion
            idx = bisect_left(potions, min_potion)
            
            # Count remaining potions
            pairs.append(m - idx)
            
        return pairs