class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        previs_sum =0
        ans =[]
        for num in nums:
            previs_sum += num
            ans.append(previs_sum)
        return ans
            