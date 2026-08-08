class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = 'aeiouAEIOU'
        start_vowel = 0
        end_vowel = len(s) - 1
        while start_vowel < end_vowel:
            if s[start_vowel] not in vowels:
                start_vowel += 1
            elif s[end_vowel] not in vowels:
                end_vowel -= 1
            else:
                s[start_vowel], s[end_vowel] = s[end_vowel], s[start_vowel]
                start_vowel += 1
                end_vowel -= 1

        return ''.join(s)