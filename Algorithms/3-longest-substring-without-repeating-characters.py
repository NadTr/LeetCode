class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub_len = 0
        sub_string = ""

        for i in range(len(s)):
            if s[i] in sub_string:
                if len(sub_string) > max_sub_len:
                    max_sub_len = len(sub_string)
                sub_string = sub_string[sub_string.index(s[i]) + 1:] + s[i]
            elif i == len(s) - 1:
                sub_string += s[i]
                if len(sub_string) > max_sub_len:
                    max_sub_len = len(sub_string)
            else:
                sub_string += s[i]
        
        return max_sub_len