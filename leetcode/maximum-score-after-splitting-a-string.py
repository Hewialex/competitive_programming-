class Solution:
    def maxScore(self, s: str) -> int:
        maxS = 0
        score = 0
        prefix = [0]

        for i in range(len(s)):
            prefix.append(prefix[i] + (s[i] == '0'))

        for i in range(1, len(s)):
            zeros_left = prefix[i]  
            ones_right = len(s) - i - (prefix[len(s)] - prefix[i])  
            score = zeros_left + ones_right
            maxS = max(maxS, score)

        return maxS
        
        
                