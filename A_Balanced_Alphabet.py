t = int(input())
for _ in range(t):
    n , k = map(int,input().split())
    ans =[]
    for _ in range(n//k):
        idx = 97
        for i in range(k):
            ans.append(chr(i+idx))
    if n%k != 0:
        for i in range(n%k):
            ans.append(chr(97+i))
    print("".join(ans))
