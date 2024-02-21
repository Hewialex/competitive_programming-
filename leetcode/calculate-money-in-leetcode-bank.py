class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        left = n % 7
        
        total = 28 * weeks + 7 * (weeks - 1) * weeks // 2
        
        if left > 0:
            total += weeks * left + left * (left + 1) // 2
        
        return total

            