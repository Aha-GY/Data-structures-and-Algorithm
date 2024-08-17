class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
         
        if len(nums1) > len(nums2):
            temp = nums2
            long = nums1
        else:
            temp = nums1
            long = nums2
        ans =[]
        for num in temp:
            if num in long:
                ans.append(num)
                i = long.index(num)
                long.pop(i)
        return ans
                