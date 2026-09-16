class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visitedx = set()
        visitedy = set()
        rows , cols = len(matrix) , len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    visitedx.add(i)
                    visitedy.add(j)
        for i in range(rows):
            for j in range(cols):
                if i in visitedx or j in visitedy:
                    matrix[i][j] = 0
