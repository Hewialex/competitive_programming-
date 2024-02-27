class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        def myPow(base,exponent):
            ans = 1
            while exponent > 0:
                if exponent % 2 == 1:
                    ans = (ans * base) % mod
                base = (base * base) % mod
                exponent //= 2
            return ans

        even = myPow(5, n//2 + n%2)
        odd = myPow(4, n//2)
        return (even*odd) % mod
