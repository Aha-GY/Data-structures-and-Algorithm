class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        odd = ""
        for i in range(len(num)):
            if int(num[i])%2:
                odd =""
                odd = num[:i+1]
        return odd