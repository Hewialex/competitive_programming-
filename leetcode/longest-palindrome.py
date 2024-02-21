class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        len = 0
        odd_count = 0
        
        for cou in count.values():
            len += cou // 2 * 2
            if cou % 2:
                odd_count = 1
        
        len += odd_count
        
        return len
            