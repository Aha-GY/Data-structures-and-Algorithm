class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        count = Counter(s)
        palindrome =0
        temp =0
        for val in count.values():
            if val%2:
                palindrome += val -1
                temp =1
            else:
                palindrome +=val
                
        return palindrome+1 if temp ==1 else palindrome