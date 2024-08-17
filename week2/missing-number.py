class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if 0 not in nums:
            return 0
        elif nums[-1]!=len(nums):
            return len(nums)
        else:
            temp_nums = nums[0]
            for i in nums[1:]:
                if  i != temp_nums + 1:
                    return temp_nums + 1
                if nums[-1] != len(nums) :
                    return len(nums)
                temp_nums +=1
            
            
        
        # i=0
        # j=1
        # print(type(nums))
        # while j < len(nums):
        #     if not nums[i] + 1 == nums[j]:
        #         return  nums[i] + 1 
        #     i+=1
        #     j+=1
        # if len(nums) == j + 1:
        #     return nums[j] + 1
