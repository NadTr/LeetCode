class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        original_board = [line[:] for line in board]
        def check_neighbors(i,j):
            neighbors_alive = 0
            range_i = range(max(0,i-1), min(m, i + 2))
            range_j = range(max(0,j-1), min(n, j + 2))
            for ii in range_i:
                for jj in range_j:
                    if ii == i and jj == j:
                        continue
                    else:
                        if original_board[ii][jj] == 1:
                            neighbors_alive += 1
            return neighbors_alive
            
        for i in range(m):
            for j in range(n):
                alives_around = check_neighbors(i,j)
                if original_board[i][j] == 1 and alives_around in [2, 3]:
                    board[i][j] = 1
                elif original_board[i][j] == 0 and alives_around == 3:
                    board[i][j] = 1
                else:
                    board[i][j] = 0