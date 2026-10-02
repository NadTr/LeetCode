class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        line = 0
        col = 0
        way = 0

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        size = [[0, len(matrix) - 1], [0, len(matrix[0]) - 1]]
        spiral = []

        change_size = {
            (0,1) : [[1,0],[0,0]],
            (1,0) : [[0,0],[0,-1]],
            (0,-1) : [[0,-1],[0,0]],
            (-1,0) : [[0,0],[1,0]]
        }
        for i in range (len(matrix) * len(matrix[0])):
            spiral.append(matrix[line][col])

            if ((way == 2  and col <= size[1][0]) or (way == 0  and col >= size[1][1]) or (way == 3  and line <= size[0][0]) or (way == 1  and line >= size[0][1])):
                change_row, change_col  = change_size[directions[way]]                  
                size = [[size[0][0] + change_row[0],size[0][1] + change_row[1]],[size[1][0] + change_col[0],size[1][1] + change_col[1]]]
                way = way + 1 if way < 3 else 0

            line += directions[way][0]
            col += directions[way][1]

        return spiral