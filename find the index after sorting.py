class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        nums1 = sorted(nums)
        for i in range(len(nums1)):
            if nums1[i]==target:
                ans.append(i)
                
        return ans
        