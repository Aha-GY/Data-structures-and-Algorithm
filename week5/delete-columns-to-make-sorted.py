class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        count =0
        for coulmn in range(len(strs[0])):
            for row in range(1,len(strs)):
                if ord(strs[row][coulmn]) < ord(strs[row-1][coulmn]):
                    count +=1
                    break
        return count
        