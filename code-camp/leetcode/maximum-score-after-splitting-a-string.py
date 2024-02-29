class Solution:
    def maxScore(self, s: str) -> int:
        
        count = Counter(s)
        curr = count["1"]
        max_score =0
        for i in range(len(s)):
            if i != len(s)-1 and s[i] == "0":
                curr +=1
            elif s[i] == "1":
                curr -=1
            max_score = max(max_score,curr)
        return max_score
        