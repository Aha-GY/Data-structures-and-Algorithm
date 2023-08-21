class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        if k == 0 or n == 0 or n == k:
            return
        
        count = 0
        start = 0
        current = start
        prev = nums[start]
        
        while count < n:
            current = (current + k) % n
            nums[current], prev = prev, nums[current]
            count += 1
            
            if current == start:
                start += 1
                current = start
                prev = nums[start]