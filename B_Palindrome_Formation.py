t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    l =0
    r = n-1
    while l<r :
        if num[l] == num[r]:
            l+=1
        else:
            r -=1