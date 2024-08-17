n,t = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
nums = nums[::-1]
prefix =[0]
temp =0
for num in nums:
    temp += num
    prefix.append(temp)
for _ in range(t):
    x ,y = map(int,input().split())
    print(prefix[x]-prefix[x-y])
    