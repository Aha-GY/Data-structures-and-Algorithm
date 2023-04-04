import math 
grades = [45,33,67,74,4,88]
res = []
for grade in grades :
            if  grade >=38 :
                mod5 = grade % 5
                if mod5 >= 3 :
                    grade +=( 5- mod5)
                    res.append(grade)
                else :
                       res.append(grade)
            else :
                   res.append(grade)
print = (f"{res}")
