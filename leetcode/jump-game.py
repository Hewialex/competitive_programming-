class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = 0
        for n in nums[:-1]:
            cur = max(cur-1, n)
            if cur <= 0:
                return False
        return True                        