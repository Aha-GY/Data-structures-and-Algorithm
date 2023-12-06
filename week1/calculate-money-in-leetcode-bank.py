class Solution:
    def totalMoney(self, n: int) -> int:
        
        i =0
        total =0
        while i<n:
            m =  i//7 + i%7
            total += m +1
            i+=1
        return total
        
