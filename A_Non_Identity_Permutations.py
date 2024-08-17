t = int(input())
for _ in range(t):
    n = int(input())

    ans =[]
    for i in range(1,n+1):
        if i%2 and i == n:
            ans.append(i)
        elif i%2:
            ans.append(i+1)
        else:
            ans.append(i-1)
    if n%2:
        ans =ans[::-1]
    print(*ans)
