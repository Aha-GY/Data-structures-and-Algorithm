class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        
        nums.sort()
        min_diff = float("inf")
        output =0
        for i in range(len(nums)):
            right = len(nums)-1
            left = i+1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                diff = abs(curr_sum - target)
                if diff <= min_diff:
                    output = curr_sum
                    min_diff = diff
                if curr_sum > target:
                    right -=1
                elif curr_sum < target:
                    left +=1
                elif curr_sum == target:
                    return curr_sum
        return output
                    
        