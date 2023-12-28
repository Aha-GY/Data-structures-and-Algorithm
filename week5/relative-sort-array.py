class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        count =  Counter(arr1)
        ans =[]
        for num in arr2:
            frq = count[num]
            while frq >0:
                ans.append(num)
                frq -=1
        temp =[]
        if len(arr1) != len(arr2):
            for num in arr1:
                if num not in arr2:
                    temp.append(num)
            temp.sort()
            ans.extend(temp)
        return ans
            