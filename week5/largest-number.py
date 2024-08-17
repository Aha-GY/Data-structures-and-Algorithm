class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        temp = []
        for num in nums:
            temp.append(str(num))
            
        for i in range(len(temp)):
            for j in range(i+1,len(temp)):
                if (temp[j] + temp[i]) > (temp[i] + temp[j]):
                    temp[j] , temp[i] = temp[i] , temp[j]
                    
        ans = ""
        for num in temp:
            ans += num
        return str(int(ans))
            
            
