class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = sum(1 for i in range(k) if s[i] in vowels)
        max_vowel_count = vowel_count

        for i in range(len(s) - k):
            if s[i] in vowels:
                vowel_count -= 1
            if s[i + k] in vowels:
                vowel_count += 1 
            if vowel_count == k: return k
            
            max_vowel_count = max(vowel_count, max_vowel_count)    

        return max_vowel_count