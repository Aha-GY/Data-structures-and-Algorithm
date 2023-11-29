class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        a =[0]*2
        a[0] = celsius + 273.15
        a[1] = celsius*1.8 +32
        return a