class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_in_first_row = False
        zero_in_first_col = False
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        zero_in_first_row = True
                    if j == 0:
                        zero_in_first_col = True                     
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if zero_in_first_row:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if zero_in_first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0