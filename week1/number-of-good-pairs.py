class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count = defaultdict(int)
        ans = 0
        for i in range(len(nums)):
            count[nums[i]] +=1
        sum_ans =0
        for i in count:
            ans = count[i] -1
            while ans >0:
                sum_ans +=ans
                ans -=1
        return sum_ans
        
       
            
        