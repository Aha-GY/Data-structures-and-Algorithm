class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        i,ans = 0,0
        j = len(piles)-2
        piles.sort()
        
        while i <j:
            ans += piles[j]
            j-=2
            i+=1
        return ans
        