class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        change ={5:0,10:0,20:0}
        for bill in bills:
            change[bill] +=1
            if bill == 10:
                change[5] -=1
                if change[5] <0:
                    return False
            elif bill == 20:
                if 10*change[10] + 5*change[5] < 15 or (change[5] ==0):
                    return False
                else:
                    if change[10] >= 1:
                        change[10] -=1
                        change[5] -=1
                    else:
                        change[5] -=3
                    
        return True