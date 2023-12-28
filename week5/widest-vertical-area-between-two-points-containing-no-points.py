class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        max_width =0
        points.sort()
        for i in range(1,len(points)):
            max_width = max(max_width, points[i][0] - points[i-1][0])
        return max_width