class Solution:
    def numberOfWays(self, s: str) -> int:
        
        n_zero ,n_one = 0,0
        prefix,sefix =[],[]
        ans =0
        for i in range(len(s)):
            if s[i] =="0":
                prefix.append(n_one)
                n_zero+=1
            else:
                prefix.append(n_zero)
                n_one +=1
        n_zero ,n_one = 0,0
        i = len(s)-1
        while i>=0:
            if s[i] =="0":
                sefix.append(n_one)
                n_zero+=1
            else:
                sefix.append(n_zero)
                n_one +=1
            i -=1
        sefix = sefix[::-1]
        
        for i in range(len(s)):
            ans += prefix[i]*sefix[i]
        return ans