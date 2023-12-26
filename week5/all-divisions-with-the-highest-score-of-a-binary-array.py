class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)
        one = count[1]
        dic ={}
        zero, sum_1_0 = 0,0 
        
        for i in range(len(nums)):
            sum_1_0 = one + zero
            dic[i] = sum_1_0
            if nums[i] ==1:
                one -=1
            else:
                zero +=1
        dic[i] = sum_1_0
        dic[i+1] = count[0]
        
        ans =[]
        max_sum = max(dic.values())
        for key,val in dic.items():
            if max_sum == val:
                ans.append(key)
        return ans