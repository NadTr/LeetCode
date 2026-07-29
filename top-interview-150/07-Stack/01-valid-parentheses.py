class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        stack = []
        for char in s:
            if char in brackets.keys():
                stack.append(char)
            elif char in brackets.values():
                if stack == []:
                    return False
                elif brackets[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        return stack == []
