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