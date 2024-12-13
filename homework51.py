import math
def ygol(n1,n2):
    c = math.acos((n1)/math.sqrt(n1**2+n2**2))
    return c
x = input('Введите координаты точки через пробел ').split()
y = input('Введите координаты точки через пробел ').split()
z = input('Введите координаты точки через пробел ').split()
x[0],x[1],y[0],y[1],z[0],z[1] = map(float, (x[0],x[1],y[0],y[1],z[0],z[1]))
q, w, e = ygol(x[0], x[1]),ygol(y[0],y[1]),ygol(z[0],z[1])
m = min(q,w,e)
if m == q:
    print(x[0],x[1])
if m == w:
    print(y[0],y[1])
if m == e:
    print(z[0],z[1])

