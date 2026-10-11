class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        col_counter = Counter(zip(*grid))
        
        equal_pairs = 0
        for r in grid:
            equal_pairs += col_counter[tuple(r)]

        return equal_pairs