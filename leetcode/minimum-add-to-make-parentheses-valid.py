class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        req_open = 0
        for char in s:
            if char == "(":
                balance += 1
            elif char == ")":
                balance -= 1
            if balance == -1:
                req_open += 1
                balance += 1
        return balance + req_open