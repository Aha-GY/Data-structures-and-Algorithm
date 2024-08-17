t = int(input())
ans = {}
for _ in range(t):
    name = str(input())
    if name not in ans:
        ans[name] = 0
        print("OK")
    else:
        ans[name] +=1
        name += str(ans[name])
        print(name)