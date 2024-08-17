class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        left= 0
        curr_sum , max_sum = 0,0
        unique_nums = set()
        for right in range(len(nums)):
            while left < right and nums[right] in unique_nums:
                curr_sum -= nums[left]
                unique_nums.remove(nums[left])
                left +=1
            unique_nums.add(nums[right])
            curr_sum += nums[right]
            max_sum = max(max_sum, curr_sum)
        return max_sum
                