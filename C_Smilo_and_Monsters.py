t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    nums = nums[::-1]
    total = sum(nums)
    cur_sum ,ans= 0, total
    
    for i in range(n):
        cur_sum += nums[i]
        total -= nums[i]
        output = 0
        if cur_sum > total:
            output = cur_sum - total
            output = (output + 1) // 2
        ans = min(ans, i + 1 + total + output)
    print(ans)

