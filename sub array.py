class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i , j in zip(l,r):
            new_nums = nums[i:j+1]
            new_nums.sort()
            flag  = False
            diff = new_nums[1] - new_nums[0]
            for h in range(len(new_nums)-1):
                if  new_nums[h+1] - new_nums[h] != diff:
                    flag = True
                    break
            if flag == True:
                ans.append(False)
            else:
                ans.append(True)
        return ans





