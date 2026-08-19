class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_line = "qwertyuiop"
        second_line = "asdfghjkl"
        third_line = "zxcvbnm"
        one_row_words = []
        for word in words:
            only_one_row = True
            line = first_line if word[0].lower() in first_line else (second_line if word[0].lower() in second_line else third_line)
            for letter in word.lower():
                if letter not in line:
                    only_one_row = False
            if only_one_row:
                one_row_words.append(word)
        return one_row_words
