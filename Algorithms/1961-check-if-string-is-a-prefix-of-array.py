class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        l = 0
        index = 0
        w = ''
        while l < len(s) and index < len(words):
            w += words[index]
            l = len(w)
            index += 1
            if s == w:
                return True
        return False