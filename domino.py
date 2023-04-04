
domino_num = 0
max_domino_num= 0 
for i in range (1,17):
    for j in range(1,17):
        domino_num = int((i*j)/2)
        if max_domino_num < domino_num :
            max_domino_num = domino_num
print(max_domino_num)