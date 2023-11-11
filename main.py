import numpy as np

a = np.array([1, 2, 3])

print(a)

b = np.zeros((3, 4))

print(b)

c = np.ones((3, 4), dtype=np.int16)

print(c, '\n')

d = np.arange(10, 30, 2)

print(d, '\n')

e = np.linspace(0, 2, 9)

print(e, '\n')

f = np.full((2, 2), 7)

print(f, '\n')

g = np.eye(4)

print(g, '\n')

h = np.random.random((2, 2))

print(h, '\n')

i = np.empty((3, 2))

print(i, '\n')

print(i.shape)
print(len(i))

print(g.ndim)

print(g.shape)
print(g.size)
print(g.dtype)
print(c.dtype)

