class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        spiral = []
        while len(matrix):
            spiral += matrix[0]
            matrix = list(zip(*matrix[1:]))[::-1]
        return spiral