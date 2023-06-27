class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ans = []

        for j in s :
             if j.isalpha() == True  or j.isdigit():
                 ans.append(j)
        return  ans == ans[::-1] 

                