class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def halfpow(base,ex):
            if ex == 0:
                return 1
            elif ex%2 ==0:
                one_part = halfpow(base,ex//2)
                return one_part**2
            else:
                one_part = halfpow(base,(ex-1)//2)
                return base*(one_part **2)
        if n<0:
            x = 1/x
            n = -n
        return halfpow(x,n)