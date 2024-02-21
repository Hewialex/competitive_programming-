class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {}
        total_rabbits = 0
        for rab in answers:
            count[rab] = count.get(rab,0) + 1
        for val , cou in count.items():
            total_rabbits += ceil(cou/(val+1)) * (val + 1)
        return total_rabbits

        