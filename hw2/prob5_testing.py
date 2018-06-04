import numpy as np
import math
import matplotlib.pyplot as plt

p = 0.5


def B(n, h):
    b = math.gamma(n+1)/(math.gamma(h+1) * math.gamma(n-h+1)) * p**h * (1-p)**(n-h)
    return b


B(10000,1.1)


xs = np.arange(1,100)
ys = [math.factorial(x) for x in xs]
plt.semilogx(xs, ys); plt.show()
