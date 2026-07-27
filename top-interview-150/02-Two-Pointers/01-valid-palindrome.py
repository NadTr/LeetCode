import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        arr = re.findall(r'[a-z0-9]', s_lower)
        end = len(arr) - 1
        for i in range(len(arr)//2):
            if arr[i] != arr[end - i]:
                return False
        return True
        