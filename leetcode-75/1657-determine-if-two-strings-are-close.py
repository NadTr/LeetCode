from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        chars1 = Counter(word1)
        chars2 = Counter(word2)
        if set(chars1.keys()) != set(chars2.keys()): 
            return False
        if sorted(chars1.values()) != sorted(chars2.values()): 
            return False
        return True
       