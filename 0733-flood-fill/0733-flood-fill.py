class Solution:
    def floodFill(self, image, sr, sc, new_color):
        rows , cols = len(image) , len(image[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        original_color = image[sr][sc]
        if original_color == new_color:
            return image
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != original_color:
                return
            image[r][c] = new_color
            for dr , cr in directions:
                dfs(r+dr,c+cr)
        dfs(sr,sc)
        return image