class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lines = ["" for _ in range(numRows)]
        line = 0
        way = 1
        for char in s:  
            lines[line] += char
            way = way if (line + way >= 0 and line + way < numRows) else -way
            line += way
        return "".join(lines)
        