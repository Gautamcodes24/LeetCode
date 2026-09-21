class Solution:
    def incrementRow(self,mat,indx):
        col = len(mat[0])
        for i in range(col):
            mat[indx][i] += 1
    def incrementCol(self,mat,indx):
        col = len(mat)
        for i in range(col):
            mat[i][indx] += 1
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        mat = [[0] * n for _ in range(m)]
        count = 0
        for r,c in indices:
            self.incrementRow(mat,r)
            self.incrementCol(mat,c)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] % 2 != 0:
                    count += 1
        return count

        
        