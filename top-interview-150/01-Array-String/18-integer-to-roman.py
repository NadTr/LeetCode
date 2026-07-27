class Solution:
    def intToRoman(self, num: int) -> str:
        
        symbols = {
            1 : "I",
            5 : "V",
            1 : "I",
            10 : "X",
            50 : "L",
            100 : "C",
            500 : "D",
            1000 : "M",
        }
        
        roman = ""
        nums = str(num)
        i = 0
        while i < len(nums):
            roman_digit = ""
            ten_value = 10 ** (len(nums) - i - 1)
            if nums[i] == "9":
                roman_digit = symbols[ten_value] + symbols[10 * ten_value]
            elif nums[i] == "4":
                roman_digit = symbols[ten_value] + symbols[5 * ten_value]
            else : 
                ones = 0
                if int(nums[i]) >= 5:
                    roman_digit = symbols[5 * ten_value]
                    ones = 5
                while ones < int(nums[i]):
                    roman_digit += symbols[ten_value]
                    ones += 1
            roman += roman_digit
                
            i += 1

        return roman