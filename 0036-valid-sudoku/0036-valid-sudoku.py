from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        sqaure = defaultdict(set)
        row = defaultdict(set)
        col = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                ele = board[i][j]
                if ele in row[i] or ele in col[j] or ele in sqaure[(i//3,j//3)]:
                    return False
                row[i].add(ele)
                col[j].add(ele)
                sqaure[(i//3,j//3)].add(ele)
        return True


        