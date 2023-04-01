class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        j = []
        for i in range (1,n+1):
            if i%3 ==0 and i%5 ==0 :
                j.append ("FizzBuzz") 
            elif i%5 == 0 :
                j.append("Buzz")
            elif i%3==0:
                j.append("Fizz")
            else:
                j.append(str(i))
        return  j         
             