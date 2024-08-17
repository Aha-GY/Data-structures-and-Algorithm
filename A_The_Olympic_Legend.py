t = int(input())
for _ in range(t):
    nums = list(map(int,input().split()))
    runner =0
    for i in range(1,len(nums)):
        if nums[i] > nums[0]:
            runner +=1
    print(runner)