t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    n -=1
    while n>= 0:
        if n + nums[n] < len(nums):
            nums[n] += nums[n+nums[n]]
        n -=1
    print(max(nums))