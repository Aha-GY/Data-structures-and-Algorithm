n = int(input())
costemer = list(map(int , input().split()))
costemer.sort()
ans = 0
serve_time =0
for num in costemer:
    if num >= serve_time:
        serve_time += num
        ans +=1
print(ans)