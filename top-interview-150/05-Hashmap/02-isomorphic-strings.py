class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        index_char_s = {}
        index_char_t = {}
        
        for i in range(len(s)):
            if s[i] in index_char_s:
                index_char_s[s[i]] += [i]
            else :
                index_char_s[s[i]] = [i]
            if t[i] in index_char_t:
                index_char_t[t[i]] += [i]
            else :
                index_char_t[t[i]] = [i]

        return list(index_char_s.values()) == list(index_char_t.values())
            

        
        