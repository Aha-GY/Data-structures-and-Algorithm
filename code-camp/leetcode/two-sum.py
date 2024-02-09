class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        temp =[0]*len(nums)
        temp[:len(nums)] = nums
        temp.sort()
        left =0
        right = len(nums)-1
        
        while left < right:
            if temp[left] + temp[right] == target:
                break
            elif temp[left] + temp[right] > target:
                right -=1
            else:
                left += 1
        ans =[]
        for i in range(len(nums)):
            if nums[i] == temp[left]:
                ans.append(i)
            elif nums[i] == temp[right]:
                ans.append(i)
        return  ans