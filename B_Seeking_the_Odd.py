t = int(input())
for _ in range(t):
    n = int(input())
    if n%2:
        print("YES")
    else:
        n = n/2
        while n >1:
            if n%2:
                print("YES")
                break
            n = n/2
        else:
            print("NO")
            
        