class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans= []
        for i in range(len(nums)):
            if i >0 and  nums[i] == nums[i-1]:
                continue 
            left = i+1
            right = len(nums)-1
            while left < right:
                temp =[]
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while left < right and  nums[left-1] == nums[left]:
                        left +=1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return ans