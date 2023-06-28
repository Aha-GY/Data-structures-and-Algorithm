class Solution:
    def reverse(self, x: int) -> int:
      

        arr = list(str(x))
        
        if x < 0 :
            x = str(x)
            arr[1:len(arr)]=arr[:0:-1]
            y=int(''.join(arr))
        else :
            x = str(x)
            y= int(x[::-1])
        if y <= -2**31 or y >= (2**31)-1:
            return 0
        else :
            return y
