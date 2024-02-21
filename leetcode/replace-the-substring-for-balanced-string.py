class Solution:
    def balancedString(self, s: str) -> int:
        counts = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        target = len(s) // 4
        replacements = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        min_length = len(s)
        left = 0

        for ch in s:
            counts[ch] += 1

        for ch in 'QWER':
            replacements[ch] = max(0, counts[ch] - target)

        for right in range(len(s)):
            ch = s[right]
            replacements[ch] -= 1

            while left < len(s) and all(replacements[ch] <= 0 for ch in 'QWER'):
                min_length = min(min_length, right - left + 1)
                replacements[s[left]] += 1
                left += 1

        return min_length