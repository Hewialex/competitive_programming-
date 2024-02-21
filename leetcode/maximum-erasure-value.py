class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxSum = 0
        currentSum = 0
        left = 0
        seen = set()
        
        for right in range(len(nums)):
            num = nums[right]
            
            while num in seen:
                seen.remove(nums[left])
                currentSum -= nums[left]
                left += 1
            
            seen.add(num)
            currentSum += num
            maxSum = max(maxSum, currentSum)
        
        return maxSum

            