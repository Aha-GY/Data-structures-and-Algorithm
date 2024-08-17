n = int(input())
a = list(map(int,input().split()))

a = a[::-1]
b = [a[0]]

for i in range(1,len(a)):
    b.append(a[i] +a[i-1])
b = b[::-1]
print(*b)