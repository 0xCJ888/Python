# midpoint rule & trapezoidal rule integrate funtion

def f1(x):
    return x + 3

def f2(x):
    return x * x + 2

def f3(x):
    return  x * (x * (x - 2) + 1) + 5

def midpoint_rule(func, xa, xb, np):
    sum = 0
    h = (xb - xa) / float(np)
    m = xa + h / 2.0
    for i in range(0, np):
        sum += func(m+h*i)
    sum *= h
    return sum

def trapezoidal_rule(func, xa, xb, np):
    h = (xb - xa) / np
    sum = func(xa) + func(xb)
    for i in range(1, np):
        sum += 2*func(xa+i*h)
    sum *= h / 2.0
    return sum

np = 10000
print("f1 = (np = 10000)")
print("midpiont rule method of f1 :", midpoint_rule(f1, 0, 1.0, np))
print("trapezoidal rule method of f1 :", trapezoidal_rule(f1, 0, 1.0, np))

np = 10000
print("f2 = (np = 10000)")
print("midpiont rule method of f2 :", midpoint_rule(f2, 0, 1.0, np))
print("trapezoidal rule method of f2 :", trapezoidal_rule(f2, 0, 1.0, np))


np = 10000
print("f3 = (np = 10000)")
print("midpiont rule method of f3 :", midpoint_rule(f3, 0, 1.0, np))
print("trapezoidal rule method of f3 :", trapezoidal_rule(f3, 0, 1.0, np))