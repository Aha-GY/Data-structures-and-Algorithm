class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        mod = 10**9 +7
        if n ==1:
            return 5
        elif n==0:
            return 1
        if n%2:
            x = pow(5,(n//2)+1,mod)
            y = pow(4,n//2,mod)
            return (x*y)%mod
        else:
            x = pow(5,n//2,mod)
            y = pow(4,n//2,mod)
            return (x*y)%mod
        
            
            
            
            
            
            
            