class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
      
        val = sorted(nums , reverse = True)
        operation =0
        max_val = val[0]
        for i in range(1,len(val)):
            if val[i] < max_val:
                operation += i
                max_val = val[i]
        return  operation  