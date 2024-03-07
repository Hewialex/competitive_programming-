class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            count = n-mid
            if citations[mid] >= count:
                right = mid  - 1
            else:
                left = mid +1   
        return n - left         