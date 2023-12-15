class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos ,neg =[],[]
        for num in nums:
            if num >0:
                pos.append(num)
            else:
                neg.append(num)
        j =0
        for p_num , n_num in zip(pos,neg):
            nums[j] = p_num
            j+=1
            nums[j] = n_num
            j+=1
        return nums
                    