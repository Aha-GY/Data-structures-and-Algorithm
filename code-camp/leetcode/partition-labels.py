class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        count = {}
        for i in range(len(s)):
            count[s[i]] = i
        max_i = count[s[0]]
        ans =[]
        prev =0
       
        for i in range(len(s)):
            max_i = max(max_i,count[s[i]])
            if max_i == i:
                ans.append(i-prev +1)
                prev = i +1 
            
        return ans