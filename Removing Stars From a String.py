class Solution:
    def removeStars(self, s: str) -> str:
        i = 0
        new_s = []
        
        while i < len(s):
            if s[i] == '*':
                new_s.pop()
            else:
                new_s.append(s[i])
            i+=1
        return ''.join(new_s)
                
        