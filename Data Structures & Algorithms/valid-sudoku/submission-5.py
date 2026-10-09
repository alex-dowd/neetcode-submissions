class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Rows
        for i in range(9):
            nums = set()
            for j in range(9):
                if board[i][j] in nums and board[i][j] != ".":
                    return False
                else:
                    nums.add(board[i][j])
        #Collumns
        for i in range(9):
            nums = set()
            for j in range(9):
                if board[j][i] in nums and board[j][i] != ".":
                    return False
                else:
                    nums.add(board[j][i])
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                nums = set()
                for a in range(i,i+3):
                    for b in range(j,j+3):
                        if board[a][b] in nums and board[a][b]!=".":
                            return False
                        else:
                            nums.add(board[a][b])
        return True
                    