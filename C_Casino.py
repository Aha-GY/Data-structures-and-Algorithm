t = int(input())
nums = list(map(int, input().split()))
ans = []

for num in nums:
    temp = num
    while temp > 1:
        if temp % 2 == 0:
            temp = temp // 2
        elif temp % 3 == 0:
            temp = temp // 3
        else:
            ans.append(temp)
            break
    else:
        ans.append(1)

if len(set(ans)) == 1:
    print("Yes")
else:
    print("No")
