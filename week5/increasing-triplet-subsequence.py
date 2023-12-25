class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        small,medim = float("inf"), float("inf")
        
        for num in nums:
            if num <= small:
                small = num
            elif num <= medim:
                medim = num
            else:
                return True
        return False
