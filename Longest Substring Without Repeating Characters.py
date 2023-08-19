class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ans = 1
        temp = ''

        for right in range(len(s)):
            while s[right] in temp:
                temp = temp[1:]

            temp += s[right]
            ans = max(ans, len(temp))
                
        return ans