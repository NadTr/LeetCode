class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return[1]
            
        last_row = [1,1]

        for i in range(1, rowIndex):
            new_row = [1] * (i + 2)
            for j in range(1, len(last_row)):
                new_row[j] = last_row[j - 1] + last_row[j]
            last_row = new_row

        return last_row