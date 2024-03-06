class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = -1, len(nums)
        arr = [-1, -1]
        
        if target not in nums:
            return arr
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        
        arr[0] = right
        
        left, right = -1, len(nums)
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        
        arr[1] = left
        
        return arr