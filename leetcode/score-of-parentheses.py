class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        dep = 0
        res = 0
        for i , k in enumerate(s):
            if k == '(':
                dep += 1
            else:
                dep -= 1
                if s[i-1] == '(':
                    res += 2**dep
        return res
            