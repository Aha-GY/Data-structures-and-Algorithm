class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 0
        last_ptr = 0
        window = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return 1
            window += nums[i]
            if window < target:
                pass
            else:
                while window >= target:
                    temp = i-last_ptr + 1
                    res = min(res, temp) if res != 0 else temp
                    window -= nums[last_ptr]
                    last_ptr += 1
        return res