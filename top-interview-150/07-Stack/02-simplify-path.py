import re
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_split = path.split("/")
        simplified_path = []
        for part in path_split:
            if part == '..':
                if simplified_path != []:
                    simplified_path.pop()            
            elif part != '' and part != '.':
                simplified_path.append(part)
        return "/" + "/".join(simplified_path)