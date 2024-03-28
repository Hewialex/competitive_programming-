class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        if len(piles) == h:
            return m
        
        def checker(speed):
            hrs = 0
            for i in piles:
                hrs += ceil(i/speed)
            return hrs

        l, r = 1, m
        while l<=r:
            mid = (l+r)//2
            if checker(mid) <= h:
                r =mid-1
            else:
                l = mid+1
        return l  
        