class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def play(turn , r , l):
            if l > r:
                return 0
            if turn:
                return max(play(not turn , r-1 , l) + nums[r] ,play(not turn , r , l+1) + nums[l])
            else:
                return min(play(not turn , r-1 , l) - nums[r] , play(not turn , r , l+1) - nums[l]) 
        return play(1,len(nums) -1 , 0) >= 0   