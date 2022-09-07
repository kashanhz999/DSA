class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROW = len(matrix)
        COL = len(matrix[0])
        
        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == target:
                    return True
        return False
        