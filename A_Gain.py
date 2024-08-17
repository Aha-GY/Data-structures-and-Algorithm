t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    temp =[0]*n
    temp[:n] = nums
    temp.sort()
    max_num = temp[-1]
    second_max = temp[-2]
    ans =[]
    for num in nums:
        if num == max_num:
            ans.append(max_num - second_max)
        else:
            ans.append(num - max_num)
    print(*ans)