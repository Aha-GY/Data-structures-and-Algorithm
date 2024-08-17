def is_almost(i):
    factors = []
    for j in range(2, int(i**0.5) + 1):
        while i % j == 0:
            factors.append(j)
            i //= j
    if i > 1:
        factors.append(i)
    return factors

n = int(input())
count = 0   
for i in range(6, n + 1):
    if len(is_almost(i)) == 2:
        count += 1

print(count)
