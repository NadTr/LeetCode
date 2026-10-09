class Solution:
    def compress(self, chars: list[str]) -> int:
        r = w = 0
        while r < len(chars):
            c = chars[r]
            c_count = 1
            r += 1
            
            while r < len(chars) and chars[r] == c:
                c_count += 1
                r += 1

            addon = c if c_count == 1 else (c + str(c_count))
            for i in range(len(addon)):
                chars[w] = addon[i]
                w += 1
        return w