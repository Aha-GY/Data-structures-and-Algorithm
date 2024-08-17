class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) <=2:
            return False
        else:
            i =0
            while i< len(arr)-1 and arr[i] < arr[i+1]:
                i +=1
            if i==0 or i+1 == len(arr):
                return False
            while i<len(arr)-1 and arr[i] > arr[i+1]:
                i+=1
            if i+1 == len(arr):
                return True
            elif i < len(arr):
                return False