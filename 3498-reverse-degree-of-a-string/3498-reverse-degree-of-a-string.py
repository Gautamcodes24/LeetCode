class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0  # 1. Initialize to 0 for summation
        
        for index, char in enumerate(s):
            string_position = index + 1  # 2. Make it 1-indexed
            
            # 3. Calculate reversed alphabet position
            reversed_alpha_pos = 123 - ord(char) 
            
            # 4. Add the product to the total sum
            ans += reversed_alpha_pos * string_position
            
        return ans