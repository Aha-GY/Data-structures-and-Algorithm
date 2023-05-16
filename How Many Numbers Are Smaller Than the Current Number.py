class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
      
        nums_list=[]
        for j in range(len(nums)):
            nums_min= len(nums)
            for i in range(len(nums)):
                if nums[j] <= nums[i]:
                    nums_min -= 1
                
            nums_list.append(nums_min)
        return nums_list






            


