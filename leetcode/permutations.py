class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []

        def backtrack():
            if len(cur) == len(nums):
                ans.append(cur[:])
                return
            for j in nums:
                if j in cur:
                    continue
                cur.append(j)
                backtrack()
                cur.pop()
        backtrack()
        return ans
        