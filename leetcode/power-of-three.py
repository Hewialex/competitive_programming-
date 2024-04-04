class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def poww(k):
            if k == 0:
                return False
            if k == 1:
                return True
            if k%3!= 0:
                return False
            return poww(k//3)
        return poww(n)
        

