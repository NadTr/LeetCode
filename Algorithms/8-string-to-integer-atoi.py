class Solution:
    def myAtoi(self, s: str) -> int:
        number = 0
        sign = 1
        found_sign = False
        start = end = None
        for i in range(len(s)):
            if start is None:
                if not found_sign and s[i] == " ":
                    continue
                elif not found_sign and s[i] in ['+', '-']:
                    sign = -1 if s[i] == '-' else 1
                    found_sign = True
                elif s[i].isdigit():
                    start = i
                elif not s[i].isdigit():
                    return 0
            elif not s[i].isdigit() and end is None:
                    end = i
        end = end if (end is not None) else len(s)
        if start is None:  return number
        sub_s = s[start:end][::-1]
        for i in range(len(sub_s)):
            number += int(sub_s[i]) * 10 **i

        number *= sign
        if number < - 2**31:
            number = -2**31
        elif number > 2**31 - 1:
            number = 2**31  - 1
        return number