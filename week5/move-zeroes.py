class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        i=0
        j=0
        while j <len(nums):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i+=1
            j+=1
