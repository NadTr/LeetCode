class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = min(len(word1), len(word2))
        word = ''
        for i in range(l):
            word += word1[i] + word2[i]
        word += word1[l:] if len(word1) > l else (word2[l:] if len(word2) > l else '')
        return word