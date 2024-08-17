t = int(input())
for _ in range(t):
    n = int(input())

    count =0
    while  n%5 ==0:        
        n = (n*4) //5
        count +=1

    while  n%3 == 0:
        n = (n*2) //3
        count +=1

    while n%2 == 0:
        n = n //2
        count +=1
        
    if n == 1:
        print(count)
    else:
        print(-1)
