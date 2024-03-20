class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i, temp in enumerate(intervals):
            temp.append(i)
        intervals.sort()
        result = [-1]*len(intervals)

        for _, end, index in intervals:
            val = bisect_left(intervals, [end])
            if val<len(intervals):
                result[index] = intervals[val][2]
        return result
                          