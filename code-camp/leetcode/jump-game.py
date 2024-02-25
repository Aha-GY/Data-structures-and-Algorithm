class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if nums[0]==0 and len(nums)!=1:
            return False 
        max_jump =0
        for i in range(len(nums)):
            if max_jump < i:
                return False
            elif nums[i] !=0:
                max_jump = max(max_jump, nums[i]+i)
        return max_jump >= len(nums)-1
