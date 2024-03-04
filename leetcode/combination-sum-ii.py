class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        ans = []
        candidates.sort()
        def backtrack(idx, curSum):
            if curSum == target:
                ans.append(res[:])
                
            i = idx
            
            while i < len(candidates):
                if  curSum < target:
                    curSum += candidates[i]
                    res.append(candidates[i])
                    backtrack(i + 1 , curSum)
                    res.pop()
                    curSum -= candidates[i]
                i += 1
                while len(candidates) > i > 0 and candidates[i] == candidates[i-1]:
                    i+=1
        
        backtrack(0, 0)
        return ans          