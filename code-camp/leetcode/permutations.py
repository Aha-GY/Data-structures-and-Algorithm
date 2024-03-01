class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans =[]
        curr =[]
        def backtrack():
            if len(curr) == len(nums):
                if curr not in ans:
                    ans.append(curr.copy())
                    return
            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtrack()
                    curr.pop()
        backtrack()   
        return ans