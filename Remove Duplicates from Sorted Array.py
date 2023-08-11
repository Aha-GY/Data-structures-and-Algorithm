class Solution(object):
    def removeDuplicates(self, nums):
        k,prevUnique = 1,nums[0]
        for i in nums:
            if i!=prevUnique:
                prevUnique = i
                nums[k] = prevUnique
                k+=1
        return k
                
