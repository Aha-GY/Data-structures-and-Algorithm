class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0

        for j in range(len(nums)):
            for i in range(len(nums)):
                if i >j and nums[i] == nums[j]:
                    ans += 1
        return ans 