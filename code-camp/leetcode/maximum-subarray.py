class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        left =0
        max_sum = nums[0]
        curr_sum = 0
        for right in range(len(nums)):            
            curr_sum += nums[right]
            max_sum = max(max_sum,curr_sum)
            while curr_sum < 0 and right >= left:
                curr_sum -= nums[left]
                left +=1
            
        return max_sum        
        