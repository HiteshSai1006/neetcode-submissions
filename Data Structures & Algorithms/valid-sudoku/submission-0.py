class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row={}
        col={}
        sudoku = True
        #row check
        for i in range(9):
            row[i] = []
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in row[i]:
                    row[i].append(board[i][j])
                else:
                    sudoku= False

        #column check:
        for i in range(9):
            col[i] = []
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] not in col[i]:
                    col[i].append(board[j][i])
                else:
                    sudoku= False
        
        # Square check
        square = {}

        for i in range(9):
            square[i] = []
            start_row = (i // 3) * 3
            start_col = (i % 3) * 3
            for r in range(start_row, start_row + 3):
                    for c in range(start_col, start_col + 3):
                        if board[r][c] == ".":
                            continue 
                        if board[r][c] not in square[i]:
                            square[i].append(board[r][c])
                        else:
                            sudoku = False
        return sudoku






                    


            
            