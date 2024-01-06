class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        stor ={}
        target ={}
        ans =[]
        if len(p) > len(s):
            return 
        for i in range(len(p)):
            stor[s[i]] = stor.get(s[i],0) +1
            target[p[i]] = target.get(p[i],0) +1
        if stor == target:
            ans.append(0)
        left =0
        for right in range(len(p),len(s)):
            stor[s[right]] = stor.get(s[right],0) +1
            stor[s[left]] -= 1
            if stor[s[left]] ==0:
                del(stor[s[left]])
            if target == stor:
                ans.append(left+1)
            left +=1
        return ans
            
        