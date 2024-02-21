class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                continue
            for j in range(i+1 , len(nums)-1):
                if nums[j] == 0:
                    continue
                summ = nums[i] + nums[j]
                ind = bisect_left(nums , summ)
                res += ind - j - 1
        return res
                    