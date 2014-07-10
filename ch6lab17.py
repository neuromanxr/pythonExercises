def function(x):
    print(x)
    x = 4.5
    y = 3.4
    print(y)

x = 2
y = 4
function(x)
print(x)
print(y)



print()

def f(x, y = 1, z = 2):
    return x + y + z

print(f(1, 1, 1))
print(f(y = 1, x = 2, z = 3))
print(f(1, z = 3))

print()

def function1():
    x = 4.5
    y = 3.4
    print(x)
    print(y)

function1()

print(x)
print(y)

print()

x = 10
if x < 0:
    y = -1
else:
    y = 1

print("y is", y)
