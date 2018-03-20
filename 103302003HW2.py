#use Secant Method find f(x) = x^2 - 2 root (割線法)
#see https://goo.gl/NCr3dC

def f(x):
    return x ** 2 - 2

x0 = 1
x1 = 1.5
totalRes = 1.0E-5


while True:
    x2 = x1 - f(x1)*(x1 - x0) / (f(x1) - f(x0))
    delta = x2 - x1
    if abs(delta) < totalRes:
        break
    x0 = x1
    x1 = x2
    

print("Approximate root:", x2)

