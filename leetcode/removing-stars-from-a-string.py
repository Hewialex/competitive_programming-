class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for cha in s:
            if cha == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(cha)
            
        return ''.join(stack)
