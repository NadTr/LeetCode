from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)
        for k, v in ransomNote_counter.items():
            if k not in magazine_counter or magazine_counter[k] < v:
                return False
        return True