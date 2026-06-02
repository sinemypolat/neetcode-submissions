from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check cols
        for i in range(9):
            col_dict = defaultdict(int)
            for j in range(9):
                num = board[j][i]
                if not num == ".":
                    col_dict[num] += 1
                    if col_dict[num] >= 2:
                        return False

        # check rows
        for i in range(9):
            col_dict = defaultdict(int)
            for j in range(9):
                num = board[i][j]
                if not num == ".":
                    col_dict[num] += 1
                    if col_dict[num] >= 2:
                        return False

        # check 3x3 squares
        for row_start in range(0,9,3):
            for col_start in range(0,9,3):
                square_dict = defaultdict(int)
                for i in range(row_start, row_start + 3):
                    for j in range(col_start, col_start + 3):
                        num = board[i][j]

                        if num != ".":
                            square_dict[num] += 1

                            if square_dict[num] >= 2:
                                return False

        return True
        