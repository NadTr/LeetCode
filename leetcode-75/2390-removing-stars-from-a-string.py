class Solution:
    def removeStars(self, s: str) -> str:
        s2 = []
        for c in s:
            if c == '*':
                s2.pop()
            else:
                s2.append(c)

        return ''.join(s2)