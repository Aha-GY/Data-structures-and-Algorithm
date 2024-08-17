t = int(input())
nums = list(map(int,input().split()))

l,r = max(nums),min(nums)
temp = l+r
sore = []
for i in range(t):
    for j in range(i+1,t):
        if nums[i] + nums[j] == temp and j not in sore and i not in sore:
            print(i+1,j+1)
            sore.append(i)
            sore.append(j)
            break