class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        opreation = ['+','-','*','/']
        stack =[]
        for i in tokens:
            
            if not i in opreation:
                stack.append(int(i))
            else:
                first = stack.pop()
                sec = stack.pop()
                if i == "+":
                    temp = sec + first
                elif i =="-":
                    temp = sec - first
                elif i =="*":
                    temp = sec * first
                elif i == "/":
                    
                    temp = int(sec/first)
                stack.append(temp)
        return stack[0]
                
        
        