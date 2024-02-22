class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        for i , char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and stack[-1] in s[i:]:
                    seen.remove(stack.pop())
                seen.add(char)
                stack.append(char)
        return ''.join(stack)     