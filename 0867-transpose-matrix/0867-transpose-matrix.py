class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # ---------------Method 1------------------
        # return [list(ele) for ele in zip(*matrix)]
        
        # ---------------Method 2------------------
        rows = len(matrix)
        cols = len(matrix[0])
        
        # 1. Create a new "empty" matrix with flipped dimensions (cols x rows)
        # This is important for handling non-square matrices (e.g., 2x3 -> 3x2)
        result = [[0 for _ in range(rows)] for _ in range(cols)]
        
        # 2. Fill the new matrix
        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]  # Swap row and column index
                
        return result