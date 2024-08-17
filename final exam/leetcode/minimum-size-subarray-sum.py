class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r,sum_nums  = 0,0,0
        ans = []
        while r <= len(nums)-1 :
            sum_nums += nums[r]
            while sum_nums >= target:
                ans.append(r-l+1)
                sum_nums -= nums[l]
                l +=1                        
            r+=1            
        return min(ans) if len(ans) !=0 else 0
            
        