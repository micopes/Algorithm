class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkValid(x, y, val):
            for i in range(9):
                if board[x][i] == val and i != y:
                    return False
                if board[i][y] == val and i != x:
                    return False
            
            for i in range((x//3)*3, (x//3)*3+3):
                for j in range((y//3)*3, (y//3)*3+3):
                    if board[i][j] == val and i != x and j != y:
                        return False


        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    flag = checkValid(i, j, board[i][j])
                    if flag == False:
                        return False
                    

        return True
