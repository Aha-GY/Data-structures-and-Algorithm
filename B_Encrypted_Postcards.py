t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())
    ans = []
    i=0
    while i<n:
        for j in range(i+1,n):
            if s[i] == s[j]:
                ans.append(s[i])
                break
        i = j
        i += 1
    output = "".join(ans)
    print(output)