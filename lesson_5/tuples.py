var = ()
print(var)
print(type(var))

var1 = tuple()

print(var1)
print(type(var1))

var2 = (1, 2, 3)
print(var2)
print(type(var2))

var3 = 1, 2, 3
print(var3)
print(type(var3))

a, b, c = var2
print(a, b, c)

a, b = b, a
print(a, b, c)

print(var2.index(1))
print(var2.count(1))
print(var2[0])

var4 = ((1, 2), (2, 3), (3, 4))
print(var4)

