n = int(input())
for _ in range(n):
    k = int(input())
    s = str(input())

    count =[]
    count_t = 0
    for i in range(len(s)):
        if s[i] !="t":
            count.append(s[i])
        else:
            count_t += 1

    
    count.append("t"*count_t)
    print("".join(count))

