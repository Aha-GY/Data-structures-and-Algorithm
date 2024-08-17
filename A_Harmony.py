t = int(input())
for i in range(t):
    n , x = map(int, input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if i != t-1:
        k = input()
    a.sort()
    b.sort()
    b = b[::-1]
    for i in range(n):
        if a[i] + b[i] > x:
            print("No")
            break
    else:
        print("Yes")