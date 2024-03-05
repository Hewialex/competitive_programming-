class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        res = []
        path = []

        def backtrack(i):
            res.append(path[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                path.append(nums[j])
                backtrack(j + 1)
                path.pop()

        backtrack(0)
        return res