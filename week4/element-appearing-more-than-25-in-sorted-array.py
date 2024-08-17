class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        count = Counter(arr)
        for fre,val in count.items():
            if val > int(len(arr)/4):
                return fre
        