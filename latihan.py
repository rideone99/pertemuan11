import math
print('tugas latihan lab 6')
#1. asli
print('\n\nnomor 1 :')
def a(x):
    return x**2

print(a(3))

#lambda
a=lambda x: (x**2)

print(a(3))

#2. asli 
print('\nnomor 2 :')
def b(x,y):
    return math.sqrt(x**2 + y**2)

print(b(6,7))

#lambda
b=lambda x,y: math.sqrt(x**2 + y**2)
print(b(6,7))

#3. asli
print('\nnomor 3 :')
def c(*args):
    return sum(args)/len(args)
print(c(5))
#lambda
c=lambda *args:sum(args)/len(args)
print(c(5))

#4. asli
print('\nnomor 4 :')
def d(s):
    return "".join(set(s))
print(d("ridwan abdulah"))
#lambda
d=lambda s: "".join(set(s))
print(d("ridwan abdulah"))