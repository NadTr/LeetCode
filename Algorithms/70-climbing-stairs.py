class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [0, 1, 2]: return n
        
        step = 0
        step1 = 1
        step2 = 2
        for step in range(3, n+1):
            step = step1 + step2
            step1 = step2
            step2 = step     
        return step
        