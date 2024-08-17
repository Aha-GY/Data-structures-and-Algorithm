class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        max_perim =0
        nums.sort()
        for i in range(2,len(nums)):
            if nums[i-2]+nums[i-1] > nums[i]:
                perim = nums[i-2]+nums[i-1]+ nums[i]
                max_perim = max(perim, max_perim)
                
        return max_perim
