class Solution:
    def minimumSteps(self, s: str) -> int:
        
        i = len(s)-1
        count =0
        zero =0
        while i>= 0:
            if s[i] == "0":
                zero +=1
            elif s[i] =="1":
                count += zero
            i-=1
        return count