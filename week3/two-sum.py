class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        sum_func = lambda x, y: x + y

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if sum_func(nums[i], nums[j]) == target:
                    ans.append(i)
                    ans.append(j)
                    return ans 
        return ans 