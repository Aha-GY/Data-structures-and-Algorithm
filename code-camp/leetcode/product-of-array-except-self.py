class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left ,right=[1],[1]
        temp = nums.copy()[::-1]
        r_l,l_r = 1,1
        
        for i in range(1,len(nums)):
            l_r *= nums[i-1]
            left.append(l_r)
            r_l *= temp[i-1]
            right.append(r_l)
            
        right = right[::-1]
        for i in range(len(left)):
            left[i] = left[i]*right[i]
        return left
        
        
        
        