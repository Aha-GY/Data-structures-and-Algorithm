class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans =[]
        curr ={}
        def backtrack(idx):
            if idx >= len(nums):
                temp =list(curr.values()).copy()
                temp.sort()
                if temp not in ans:
                    ans.append(temp.copy())
                return 
            if idx not in curr.keys():
                curr[idx] = nums[idx]
            backtrack(idx+1)
            curr.pop(idx)
            backtrack(idx+1)
        backtrack(0)
        return ans
            
        