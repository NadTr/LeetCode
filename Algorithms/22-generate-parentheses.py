class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        p_list = []

        def add_a_parenthese(open_cnt, closed_cnt, parentheses): 
            print(parentheses)
            if len(parentheses) == 2*n and closed_cnt == open_cnt:
                p_list.append(parentheses)
            if open_cnt < n:
                add_a_parenthese(open_cnt + 1, closed_cnt, parentheses + "(")    
            if open_cnt > closed_cnt:
                add_a_parenthese(open_cnt, closed_cnt + 1, parentheses + ")")   

        add_a_parenthese(0,0,"")
        return p_list
