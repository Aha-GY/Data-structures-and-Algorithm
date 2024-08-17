class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        i =0
        j = len(s)-1
        def revers(s,i,j):
            
            if i>=j:
                return 
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
            revers(s,i,j)
        revers(s,i,j)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    