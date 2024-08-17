class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        freq = 0
        val = 1
        output = []
        while val <len(nums):
            temp = nums[freq]
            while temp > 0:
                output.append(nums[val])
                temp-=1
            freq +=2
            val +=2
        return output
        