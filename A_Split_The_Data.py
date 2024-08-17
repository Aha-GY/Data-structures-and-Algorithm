t = int(input())
m = int(input())
ans = []
for _ in range(t):
    temp = int(input())
    ans.append(temp)
ans.sort(reverse = True)
count = 0
i=0
while m>0 and i< t:
    m -= ans[i]
    count +=1
    i+=1
print(count)




