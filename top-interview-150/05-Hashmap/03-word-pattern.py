class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern) :
            return False
        pattern_to_s = {}
        s_to_pattern = {}
        for i in range(len(pattern)):
            char = pattern[i]
            word = s[i]
            if char in pattern_to_s and pattern_to_s[char] != word:
                return False
            if word in s_to_pattern and s_to_pattern[word] != char:
                return False
            pattern_to_s[char] = word
            s_to_pattern[word] = char
        return True