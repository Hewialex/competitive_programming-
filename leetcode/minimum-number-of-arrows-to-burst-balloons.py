class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        arrow = 1
        end = points[0][1]
        for i in range(1 , len(points)):
            start , stop = points[i]
            if start > end:
                arrow += 1
                end = stop
        return arrow
        