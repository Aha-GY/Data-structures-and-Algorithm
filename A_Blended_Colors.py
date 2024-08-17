t = int(input())
for _ in range(t):
    n= int(input())
    first_row = str(input())
    second_row = str(input())
    i=0
    

    while i<n:
        if first_row[i] =="R" and second_row[i] !="R":
            print("NO")
            break
        elif first_row[i] !="R" and second_row[i] =="R":
            print("NO")
            break
        i+=1
    else:
        print('YES')
    