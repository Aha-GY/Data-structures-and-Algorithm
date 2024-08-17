t = int(input())
for _ in range(t):
    b = str(input())
    i=0
    a = ""
    while i<len(b):
        if i >1 and i%2==0:
            i+=1
        a+= b[i]
        i+=1
    print(a)