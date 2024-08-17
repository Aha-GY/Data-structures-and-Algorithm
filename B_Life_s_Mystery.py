s = str(input())
stack =[]
i =0
while i < len(s):   
    while stack and stack[-1] == s[i]:
        stack.pop()
        break
    else:
        stack.append(s[i])
    i+=1
print("".join(stack))
