class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left =0 
        ans =[]
        right = len(numbers)-1
        while left < right:
            sum_num = numbers[left] + numbers[right]
            if  sum_num == target:
                ans.append(left+1)
                ans.append(right+1)
                return ans
            elif sum_num > target:
                right -=1
            else:
                left +=1
        