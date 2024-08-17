t = int(input())
nums = list(map(int,input().split()))
ans =0
max_num = max(nums)
for i in range(t):
    diff = max_num - nums[i]
    ans += diff
print(ans)