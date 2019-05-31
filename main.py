import math
import time
from numpy import np

n = 0  # global number
a = 0  # lower interval
b = 1  # upper interval


class gauss:
    def legendre(n, x):
        start = time.time()
        x = []
        if (n == 0):
            n += 1
            x = x + [1]
            return (x, start)
        elif (n == 1):
            n += 1
            x = x + [x]
            return (x)
        if (n < 10):
            n += 1
            x = x + [(((2.0 * n - 1.0) * x * legendre(n - 1, x) - (n - 1) * legendre(n - 2, x)) / n)]
            return (x)

    ###############################################
    def dlegendre(n, x):
        x = []
        if (n == 0):
            n += 1
            x = x + [1]
            return (x)
        elif (n == 1):
            n += 1
            x = x + [x]
            return (x)
        if (n < 10):
            n += 1
            x = x + [(n / (x ** 2 - 1.0)) * (x * Legendre(n, x) - Legendre(n - 1, x))]
            return (x)

    ################################################
    # order is order of the legendre polynomial to be used
    def legendreRoot(order, t=1e-20):
        if (order < 2):
            e = 1  # with out root
        else:
            root = []
            for i in range((1, int(order) / 2 + 1)):
                x = (math.cos((math.pi) * (i - 0.25) / (order + 0.5)))
                e = 10 * t
                iters = 0
                while (e > t) and (iters < 1000):
                    dx = -((legendre(order, x)) / (dlegendre(oder, x)))
                    x = x + dx
                    iters += 1
                    e = abs(dx)
                    root.append(x)
                    root = root + [root]
                    if ((order) % 2 == 0):
                        root = numpy.concatenate((-1 * root, root[::-1]))
                    else:
                        root = numpy.concatenate((-1 * root, [0, 0], root[::-1]))
                        e = 0  # determine root
            return [root, e]


####################################################
def gaussweight(order):
    w = []
    [xi, e] = legendreRoot(order)
    if (e == 0):
        w = (2 / ((1 - xi ** 2) * (dlegendre(order, xi) ** 2)))
        e = 0
    else:
        e = 1
    return [w, xi, e]
    #####################################################


def quadraure(func, order, a, b):
    [ws, xs, e] = gaussweight(order)
    if (e == 0):
        ans = ((b - a) * 0.5) * (sum(ws * func((b - a) * 0.5 * xs + (b + a) * 0.5)))
    else:
        e = 1
        ans = None
    return [ans, e]
    #####################################################


def func(x):
    func = ((math.pow(x, 3) / (x + 1)) * (math.cos(math.pow(x, 2))))  # function
    end = time.time()
    return (func(), end)
    #######################################################


def time():
    ti = end - start
    return (ti)


# end of class
# start of main program
g = gauss()
g.func()
g.legendre()
g.dlegendre()
g.legendreRoot()
g.quadraure()
g.gaussweight()
g.time()
porder = 5
[ws, xs, e] = gausslegendreweight(porder)
if (e == 0):
    print("order : ", porder)
    print("root :", xs)
    print("weight :", ws)
else:
    print("failed")
[ans, e] = quadrature(func, porder, a, b)
if (e == 0):
    print("answer of intergral :", ans)
    print("time is :", ti)
else:
    print("failed")
    print("time is :", ti)

