class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return[[1]]

        pascal_tri = [[1],[1,1]]
        last_row = pascal_tri[-1]

        for _ in range(2, numRows):
            new_row = [1]
            for i in range(len(last_row) - 1):
                new_row.append(last_row[i] + last_row[i + 1])
            new_row.append(1)
            pascal_tri.append(new_row)
            last_row = new_row
        
        return pascal_tri