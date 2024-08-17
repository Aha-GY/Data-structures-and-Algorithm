class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        count ={"W":0,"B":0}
        for i in range(k):
            count[blocks[i]] +=1
        min_white = count["W"]
        left =0
        for right in range(k,len(blocks)):
            count[blocks[right]] +=1
            count[blocks[left]] -=1
            min_white = min(min_white,count["W"])
            left +=1
        return min_white
            