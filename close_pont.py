class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []

        for index, point in enumerate(points):
            d = (point[0]**2 + point[1]**2)**.5
            ans.append([d,point])
        ans.sort()
        new_ans = []

        # for d, i in ans[:k]:
        #     new_ans.append(points[i])
        for d, point in ans[:k]:
            new_ans.append(point)
        return new_ans
            


        


        