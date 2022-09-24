class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        
        rowZero = False
        
        for i in range(0,ROWS):
            if matrix[i][0] == 0:
                rowZero = True
            for j in range(1,COLS):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(ROWS-1,-1,-1):
            for j in range(1,COLS):
                if matrix[i][0] ==0 or matrix[0][j]==0:
                    matrix[i][j] =0
            if rowZero == True:
                matrix[i][0] = 0
                