class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        output = []
        j = len(s)-1
        while j>= 0:
            if s[j] == "#":
                ord_ch = int(s[j-2:j]) + ord("a") -1
                j-=3
            else:
                ord_ch = int(s[j]) + ord("a") -1
                j -=1
            output.append(chr(ord_ch))
        return "".join(output[::-1])
