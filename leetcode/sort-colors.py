class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = 0
        cur = 0
        r = len(nums) - 1

        while cur <= r:
            if nums[cur] == 0:
                nums[cur], nums[l] = nums[l], nums[cur]
                l += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1