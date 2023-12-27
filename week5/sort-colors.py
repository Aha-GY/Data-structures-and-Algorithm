class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        
        for i in range(len(nums)):
            j =1
            while j < len(nums)-i:
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1],nums[j]
                j+=1