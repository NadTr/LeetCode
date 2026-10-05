class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes_row = set()
        zeroes_col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroes_row.add(i)
                    zeroes_col.add(j)
        
        for z in zeroes_row:
            for j in range(len(matrix[0])):
                matrix[z][j] = 0
                
        for i in range(len(matrix)):
            for z in zeroes_col:
                matrix[i][z] = 0
        