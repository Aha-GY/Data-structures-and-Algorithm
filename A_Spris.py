a = int(input())
b = int(input())
c = int(input())

for i in range(a,-1,-1):
    if i *4 <= c and i*2 <= b:
        print(i + i*2 + i*4)
        break