"""
HW3 Helper File.

Thermal & Statistical Physics
Due 2/15/18
"""

# Packages
import numpy as np
import matplotlib.pyplot as plt
import math


# PROBLEM 1

# 1B




















# PROBLEM 4

# 4B
def q_N(t):
    return 1/np.exp(1/t)


ts = np.arange(0, 1, 0.001)
ys = q_N(ts)

plt.plot(ts, ys)
plt.xlabel(r'$\tau$')
plt.ylabel(r'$\frac{q}{N}$')
plt.savefig('4b.png')
plt.show()

# This seems like it's going in the wrong direction.



def lnOmega(N):
    q = N * q_N(0)
    lnO = q * (math.log(N) - math.log(q))
    return lnO

N = 1 #?????

lnOmega(N)

# Still doesn't make sense.


# The End
