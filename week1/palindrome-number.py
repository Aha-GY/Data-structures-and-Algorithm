class Solution:
    def isPalindrome(self, x: int) -> bool:
    
        x_str = str(x)
        
    
        char = list(x_str)
        
        
        temp = char[::-1]
        
    
        return x_str == ''.join(temp)

        