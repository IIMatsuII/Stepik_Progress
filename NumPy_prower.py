from numpy import *

a = array([2,3,4])

print(a.shape)

b = array([(1.5, 2, 3), (4, 5, 6)])

print(b.shape)

z = zeros((3, 2))
print(z)

r = arange(10, 30, 5)
print(r)

l = linspace(0, 2, 9)
print(l)

b = arange(12).reshape(4, 3)
print(b)

a = array([10,20,30])
b = arange(3)
print(a)
print(b)

print(a + b)
print(a - b)

print(a ** 2)

o = 2 * sin(a)
print(o)

q = a < 20
print(q)