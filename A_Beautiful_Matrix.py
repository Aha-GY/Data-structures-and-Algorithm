n = int(input())
for _ in range(n):
    nums= list(map(int,input().split()))
    count = 0
    ans = 0
    for i in range(3):
        if nums[i] == 1:
            count+=1
    if count >=2:
        ans +=1
print(ans)