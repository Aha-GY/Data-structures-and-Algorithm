class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set =set(nums)
        start =[]
        for num in nums:
            if num -1 not in nums_set:
                start.append(num)
                
        max_count =0
        for num in start:
            count = 0
            while num in nums_set:
                num +=1
                count +=1
            max_count = max(max_count,count)
        return max_count
        
        
                

       