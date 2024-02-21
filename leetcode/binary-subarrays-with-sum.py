class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix = {0: 1}  
        curr_sum = 0

        for num in nums:
            curr_sum += num
            count += prefix.get(curr_sum - goal, 0)
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

        return count