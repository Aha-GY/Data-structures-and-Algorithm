class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        fre = Counter(nums)
        for i in fre:
            if fre[i] > len(nums)//2:
                return i