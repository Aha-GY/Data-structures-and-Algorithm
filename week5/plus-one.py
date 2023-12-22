class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digit = ""
        for num in digits:
            digit += str(num)
        ans = list(str(int(digit) +1))
        for i in range(len(ans)):
            ans[i] = int(ans[i])
        return ans
       