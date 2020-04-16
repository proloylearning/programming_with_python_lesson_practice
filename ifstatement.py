x = 2
y = 7
z = 10

if x > y:
    print(x, 'is greater than', y)
if x < y:
    print(x, 'is less than', y)
if x == y:
    print(x, 'is same as', y)
if x != y:
    print(x, 'is not same as', y)
if z > y > x:
    print(z, 'is greater than', y, 'which is greater than', x)

if x < y:
    print(x, 'is less than', y)
else:
    print(x, 'is not less than', y)

if x < y and x < z:
    print('something here was the case')
elif x < z:
    print(x, 'is less than', z)
elif y < z:
    print(y, 'is less than', z)
else:
    print('nothing was the case')
