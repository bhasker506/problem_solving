def square(x):
    x = x+1
    return x*x

def square2(x):
    x = x+2
    return square(x)

x = 10
print(square(10))
print(x)