class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        cope_nums = nums.copy()
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                nums[i] = nums[i-1]
                cope_nums[i-1] = cope_nums[i] 
                break
            
        return nums == sorted(nums ) or cope_nums == sorted(cope_nums)
