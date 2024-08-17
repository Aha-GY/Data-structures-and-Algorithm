class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = ("a","e","i","o","u")
        curr_vowel =0
        
        for right in range(k):
            if s[right] in vowels:
                curr_vowel +=1
        max_vowel = curr_vowel
        left =0
        for right in range(k,len(s)):
            if s[right] in vowels:
                curr_vowel +=1
            if s[left] in vowels:
                curr_vowel -=1
            max_vowel = max(max_vowel, curr_vowel)
            left +=1
        return max_vowel