s = str(input())
stack =[]
count =0
for che in s:
    if che =="(":
        stack.append(che)
    elif stack and stack[-1] == "(":
        count +=2
        stack.pop()

print(count)