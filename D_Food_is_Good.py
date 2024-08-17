t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int , input().split()))
    simon = sum(nums)
    curr_sum =0
    k = 1
   
    for i in range(n):
        curr_sum += nums[i]
        if i != n-1 and  curr_sum >= simon:
            print("NO")
            k = 0
            break
    if k == 1:
        for i in range(n):
            curr_sum -= nums[i]
            if i != n-1 and  curr_sum >= simon:
                print("NO")
                break
        else:
            print("YES")    