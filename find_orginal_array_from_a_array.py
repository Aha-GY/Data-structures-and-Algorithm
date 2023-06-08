class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:
            return []
        count=Counter(changed)
        ans=[]
        changed.sort()
        for i in range(len(changed)):
            if changed[i]==0:
                if count[changed[i]]!=0 and count[changed[i]]%2==0:
                    ans.append(changed[i])
                    count[changed[i]]-=2
            elif 2*changed[i] in count and count[changed[i]]>0 and count[2*changed[i]]>0:
                ans.append(changed[i])
                count[changed[i]]-=1
                count[2*changed[i]]-=1
        if sum(count.values())!=0:
            return []
        return ans

        

        


    
            
        
        
            
        

