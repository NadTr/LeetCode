class Solution:
    def isHappy(self, n: int) -> bool:
        number = n
        cycle = set()    
        while number != 1 and number not in cycle:
            new_number = 0
            for num in str(number):
                new_number += int(num)**2
            cycle.add(number)
            number = new_number        
        return number == 1