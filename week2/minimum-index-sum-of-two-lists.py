class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        output = float("inf")
        ans = []
        commen = []
        for i in list1:
            if i in list2:
                commen.append(i)

        for i in commen:
            x = list2.index(i) + list1.index(i)
            if x < output:
                output = x
                ans.clear()
                ans.append(i)
            elif x == output:
                ans.append(i)

        return list(set(ans))

