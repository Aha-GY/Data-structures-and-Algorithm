palindromic =[]
for i in range(1,400001):
    if str(i) == str(i)[::-1]:
        palindromic.append(i)

print(len(palindromic))
dp = [0]*(40000+1)
dp[0]=1
for num in palindromic:
    for i in range(40000+1):
        if i-num >= 0:
            dp[i]+=dp[i-num]

t =nt(input())
for _ in range(t):
    n = int(input())
    print((dp[n]))