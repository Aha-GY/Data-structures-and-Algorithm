class Solution:
    def isHappy(self, n: int) -> bool:
        
        while n>9:
            sum_n =0
            str_n = str(n)
            for i in range(len(str_n)):
                sum_n += int(str_n[i])**2
            n=sum_n
                
            
        if n == 1 or n ==7:    
            return True
        else:   
            return False