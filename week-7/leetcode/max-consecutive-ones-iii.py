class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        max_windo , zero_count = 0,0
        left =0
        
        for right in range(len(nums)):
            if nums[right] ==0:
                zero_count +=1
            while left <= right and zero_count > k:
                if nums[left] == 0:
                    zero_count -=1
                left +=1
            max_windo = max(max_windo , right-left+1)
        return max_windo
        