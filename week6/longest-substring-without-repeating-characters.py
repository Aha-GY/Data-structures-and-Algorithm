class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        uniq = set()
        right =0
        left =0
        longest =0
        while right < len(s):
            
            while right < len(s) and s[right] not in uniq:
                uniq.add(s[right])
                right +=1
            longest = max(longest , len(uniq))
            uniq.remove(s[left])
            left +=1
        return longest