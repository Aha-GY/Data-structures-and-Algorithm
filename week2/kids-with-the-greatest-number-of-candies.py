class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        output = []
        max_candie = max(candies)
        for i in candies:
            if i +  extraCandies >= max_candie:
                output.append(True)
            else:
                output.append(False)
        return output
        