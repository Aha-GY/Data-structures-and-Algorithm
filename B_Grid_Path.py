t = int(input())
for _ in range(t):
    x,y,k = map(int,input().split())

    if x == 1 or y == 1:
        if max(x-1,y-1) == k:
            print("YES")
        else:
            print("NO")
    elif (y-1) +(x-1)*y == k:
        print("YES")
    else:
        print("NO")