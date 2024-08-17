class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        count =0
        left =0
        right = len(nums)-1
        nums.sort()
        while right > left:
            if nums[left] + nums[right] >= target:
                right -=1
            elif nums[left] + nums[right] < target:
                count += right - left
                left +=1
        return count
        