class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        for number in range(0, x):
            if (number + 1) * (number + 1) > x:
                return number
        