class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = [0] * 26  
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            
        stack = []  
        seen = [False] * 26 
        
        for i in range(len(s)):
            if seen[ord(s[i]) - ord('a')]:
                freq[ord(s[i]) - ord('a')] -= 1
                continue
                
            while stack and stack[-1] > s[i] and freq[ord(stack[-1]) - ord('a')] > 0:
                seen[ord(stack[-1]) - ord('a')] = False
                stack.pop()
                
            stack.append(s[i])
            seen[ord(s[i]) - ord('a')] = True
            freq[ord(s[i]) - ord('a')] -= 1
            
        ans = ""
        while stack:
            ans += stack.pop()
        return ans[::-1]
