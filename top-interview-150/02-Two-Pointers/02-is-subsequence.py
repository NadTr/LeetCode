class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for i in range(len(s)):
            t_part = t[index:]
            if s[i] in t_part:
                index += t_part.index(s[i]) + 1
            else:
                return False
        return True