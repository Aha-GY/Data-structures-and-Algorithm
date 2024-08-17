class Solution:
    def romanToInt(self, s: str) -> int:
        
        ans = 0
        roman = {'I':1 ,'V':5 , 'X':10, 'L':50 ,'C':100, 'D':500 ,'M':1000 }
        i = 1
#         M C M X C I V
#         0 1 2 3 4 5 6
        
        for j in range(len(s)):
            if j == len(s)-1:
                ans += roman[s[j]]
            elif roman[s[i]] > roman[s[j]]: 
                ans -= roman[s[j]]
            else:
                ans += roman[s[j]]
            i += 1
            
        return ans