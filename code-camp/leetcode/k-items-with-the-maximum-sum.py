class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        
        if k <= numOnes:
            return k
        elif numOnes + numZeros >= k:
            return numOnes
        elif numOnes + numZeros +numNegOnes >= k:
            temp = numOnes + numZeros
            total = numOnes
            while temp <k:
                temp +=1
                total -=1
            return total
        