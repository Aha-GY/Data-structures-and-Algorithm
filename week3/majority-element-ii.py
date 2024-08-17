class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        output =[]
        fre = Counter(nums)
        for key,val in fre.items():
            if val > len(nums)//3:
                output.append(key)
        return output
        