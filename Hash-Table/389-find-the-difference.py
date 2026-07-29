from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)
        for k, v in t_count.items():
            if s_count[k] != v:
                return k