t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    check ={}
    for i in range(n):
        if nums[i] in check:
            if i - check[nums[i]] >= 2:
                print("YES")
                break
        else:
            check[nums[i]] =i
    else:
        print("NO")

