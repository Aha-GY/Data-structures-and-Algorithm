class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        l,r=0,0
        ans =0
        while r<len(nums):
            
            if nums[r] == 0:
                l=r+1
            ans = max(ans,r-l+1)
            r+=1
        return ans
            
        