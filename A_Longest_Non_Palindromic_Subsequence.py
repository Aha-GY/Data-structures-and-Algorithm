t = int(input())
for _ in range(t):
    s = str(input())
    
    if len(set(s))==1:
        print(-1)
        continue
    else:
        print(len(s)-1)