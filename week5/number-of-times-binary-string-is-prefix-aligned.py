class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        count,ans,cur_max =0,0,0
    
        for num in flips:
            cur_max = max(num,cur_max)
            count +=1 
            if count == cur_max:
                ans +=1
        return ans
            
        