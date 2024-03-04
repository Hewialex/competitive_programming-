class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        res = []
        ans = []
        def backtrack(i, curSum):
            if curSum == target:
                ans.append(res[:])
                return
            
            for j in range(i, n  ):
                if  curSum <= target:
                    curSum += candidates[j]
                    res.append(candidates[j])
                    backtrack(j , curSum)
                    res.pop()
                    curSum -= candidates[j]
        
        backtrack(0, 0)
        return ans          