class Solution:
    def trailingZeroes(self, n: int) -> int:
        divisor = 5
        trailing_zeroes = 0

        while n >= divisor:
            trailing_zeroes += n // divisor
            divisor *= 5
        
        return trailing_zeroes
