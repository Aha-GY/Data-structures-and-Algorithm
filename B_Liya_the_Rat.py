s= input()
t = int(input())
temp =[0]
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        temp.append(1)
    else:
        temp.append(0)
prefix =[]
total =0
for num in temp:
    total += num
    prefix.append(total)
for _ in range(t):
    l,r = map(int,input().split())
    print(abs(prefix[r-1] - prefix[l-1]))


