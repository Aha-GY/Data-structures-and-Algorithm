class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        a = [0]*( len(s) + 1)
        for st , en, di in shifts:
            if di == 0:
                a[st] -= 1
                a[en +1] += 1  
            elif di == 1:
                a[st] += 1
                a[en +1] -= 1  
        
        out_put = []
        for i in range(len(s)):
            if i != 0:
                a[i] += a[i-1]  
            temp = (ord(s[i]) + a[i] - ord('a')) % 26 + ord('a')
            out_put.append(chr(temp))
        return "".join(out_put)
