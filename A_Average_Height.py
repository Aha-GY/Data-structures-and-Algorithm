n = int(input())
for _ in range(n):
    t = int(input())
    nums = list(map(int,input().split()))
    for i in range(t):
        if not i%2:
            nums.append(nums[i])
            nums.pop(i)
    print(nums)
            

