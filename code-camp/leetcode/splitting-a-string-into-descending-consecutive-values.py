class Solution:
    def splitString(self, s: str) -> bool:
        
        ans =[]
        idx =0
        def backtrack(idx):
            if idx == len(s):
                for i in range(1,len(ans)):
                    if ans[i-1] - ans[i] != 1:
                        return False
                return True if len(ans) >1 else False
            else:
                for i in range(1,len(ans)):
                    if ans[i-1] - ans[i] != 1:
                        return False
                    
            for i in range(idx+1,len(s)+1):
                curr_num = s[idx:i]
                ans.append(int(curr_num))
                if backtrack(i) == True:
                    return True
                ans.pop()
            return False
        return backtrack(idx)
        