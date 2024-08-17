# class vector:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def __str__()
# v = vector(1,2)
# print(v)
# a = map(int,[1,2,3])
# print(next(a))
# print(next(a))

def gen( ):
    print(".............")
    yield()
    print(".............")
    yield
my_gen = gen()
print(my_gen)
print(next(my_gen))
print(next(my_gen))