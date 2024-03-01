class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans =[]
        curr =[]
        def backtrack(idx):
            if idx >= len(nums):
                ans.append(curr.copy())
                return 
            curr.append(nums[idx])
            backtrack(idx+1)
            curr.pop()
            backtrack(idx+1)
        backtrack(0)
        return ans