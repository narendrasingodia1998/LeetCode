class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Brute Force
        #Checking for column
        for row in range(9):
            check=[0]*10
            for col in range(9):
                if board[row][col] !=".":
                    ele=ord(board[row][col])-ord("0")
                    if check[ele]:
                        print(row,col)
                        return False
                    check[ele]=1
        #Checking for row
        for col in range(9):
            check=[0]*10
            for row in range(9):
                if board[row][col]!=".":
                    ele=ord(board[row][col])-ord("0")
                    if check[ele]:
                        return False
                    check[ele]=1
        #Checking for 3*3 box
        for i in range(3):
            for j in range(3):
                check=[0]*10
                for row in range(3):
                    for col in range(3):
                        if board[i*3+row][j*3+col]!=".":
                            ele=ord(board[i*3+row][j*3+col])-ord("0")
                            if check[ele]:
                                return False
                            check[ele]=1
        return True