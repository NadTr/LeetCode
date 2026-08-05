class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        number = str(abs(x))

        reversed_number = sign * int(number[::-1])
        
        if reversed_number < -2**31 or reversed_number > 2**31 - 1:
            return 0
        return reversed_number