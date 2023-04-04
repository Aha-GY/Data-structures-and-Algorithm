import math 
grades = [45,33,67,74,4,88]
res = []
for grade in grades :
    if  grade >=38 and grade % 5>=3:
        grade +=( 5- grade % 5)
    res.append(grade)
print(res)
