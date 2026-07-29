from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        odd = False
        for v in count.values():
            if not odd and v%2:
                length += 1
                odd = True
            length += v//2 *2
        return length