class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        output_arr = [-1] * n
        stack = []
        
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                output_arr[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)
        
        return output_arr
