class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        odd =0
        left,right =0,0
        cnt,ans = 0,0
        while right < len(nums):
            if nums[right]%2:
                odd +=1
                cnt =0
            while odd ==k:
                cnt +=1
                odd -= nums[left] &1
                left +=1
                
            ans += cnt
            right +=1
        return ans
    