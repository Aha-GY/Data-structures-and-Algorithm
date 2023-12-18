class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        less,equal,great =[],[],[]
        for num in nums:
            if num == pivot:
                equal.append(num)
            elif num > pivot:
                great.append(num)
            elif num < pivot:
                less.append(num)
        
        nums.clear()
        nums += less
        nums += equal
        nums += great
        return nums