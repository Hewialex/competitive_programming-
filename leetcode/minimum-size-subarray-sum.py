class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        windowSum = 0
        minL = float('inf')

        for right in range(n):
            windowSum += nums[right]

            while windowSum >= target:
                minL = min(minL, right - left + 1)
                windowSum -= nums[left]
                left += 1

        if minL == float('inf'):
            return 0
        else:
            return minL
            