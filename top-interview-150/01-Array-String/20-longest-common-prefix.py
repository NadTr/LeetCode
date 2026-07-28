class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        compare = strs[0]
        for i in range(len(compare)):
            for word in strs:
                if len(word) -1 < i or word[i] != compare[i]:
                    return result
            result += compare[i]
        return result