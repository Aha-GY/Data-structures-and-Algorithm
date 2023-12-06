class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        r ,l= 0,0
        output =""
        while r < len(num):
            if num[r] != num[l]:              
                l = r
            else:
                if r-l ==2:
                    output = max(output , num[l:r+1])
                    l+=1
                r+=1
        return output

