class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max = 0
        for i in range(len(nums)//2):

            sum_nums = nums[i] + nums[-i-1]
            if max < sum_nums :
                max = sum_nums
        return max