class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        ast_stack = []

        for curr in asteroids:
            add_curr_to_stack = True       
            while add_curr_to_stack and ast_stack and curr < 0 < ast_stack[-1]:
                prev = ast_stack[-1]
                if -curr > prev:
                    ast_stack.pop()
                    continue
                elif -curr == prev:
                    ast_stack.pop()
                add_curr_to_stack = False

            if add_curr_to_stack:
                ast_stack.append(curr)
        
        return ast_stack