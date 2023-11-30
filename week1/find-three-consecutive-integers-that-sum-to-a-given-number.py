class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        ans = []
        temp = num//3
        if temp*3 == num :
            ans.append(num//3 -1)
            ans.append(num//3)
            ans.append(num//3 +1)
            return ans
        else:
            return []