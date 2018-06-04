"""
Thermal PHYS
PS9
4.19.18
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import astropy.constants as c
import astropy.units as u


# Problem 2
# Excessive, but a chance to play with DataFrames.

# SET UP THE DATA
row_1 = {
        'Temp': 50 - 273,
        'Pressure': 0.1234,
        'L': 42.92
        }

row_2 = {
        'Temp': 100 - 273,
        'Pressure': 1.013,
        'L': 40.66
        }

row_3 = {
        'Temp': 150 - 273,
        'Pressure': 4.757,
        'L': 38.09
        }

rows = []
rows.append(row_1); rows.append(row_2); rows.append(row_3)
df = pd.DataFrame(rows)

df.describe()

# ADD THE MODELED VAPUR PRESSURE

def vapur_pressure_eqn(k, L, T):
    P = k * np.exp(-L/(R*T))
    return P

# Set some constants
R = c.R.value
k = 10

model_Pvs = []
for i in range(len(df)):
    pv = vapur_pressure_eqn(k, df.L[i], df.Temp[i])
    model_Pvs.append(pv)

df.assign(Pv = model_Pvs)

df


# PLOTS
# Model
plt.plot(df.Temp, model_Pvs, '-g')
# Data
plt.plot(df.Temp, df.Pressure, 'or')
plt.show()






### PROBLEM 3 ###

"""
We wish to estimate Rc for a common case, such as water at atmospheric pressure.
The boiling temperature Tb = 373 K. We also need to know the density ρ =
0.95 g/cm3 and surface tension γ = 59 × 10−3 J/m2
, which are both nearly
constant near Tb. The chemical potential difference can be estimated by
∆µ ≈ L
∆T
Tb
,
where ∆T = Tb − T. In other words, the chemical potential difference grows
linearly in temperature, and in proportion to the latent heat L = 2260 kJ/kg.
Based on these data, plot Rc near (below) the boiling temperature. Be careful
with units. You will see that Rc drops very quickly as we go below Tb, so it is
helpful to plot Rc on a logarithmic scale (LogPlot in Mathematica).
"""

# Constants:
Tb = 373 * u.Kelvin
rho = 0.95 * u.g * (u.cm)**-3
gamma = 59e-3 * u.Joule * (u.m)**-2
L = 2260 * u.kJ/u.kg
n_l = 1

Tb.value

def get_Rc(T):
    dT = Tb - T*u.Kelvin
    dMu = (L * dT)/Tb
    return 2*gamma/(n_l * dMu).decompose()


u.Joule.represents

get_Rc(300)


Rcs = []
Ts = np.arange(300,372)
for T in Ts:
    rc = get_Rc(T)
    Rcs.append(rc.value)


plt.loglog(Ts, Rcs)
plt.show()





"""
Using the above expression for Rc, plug it into the equation for ∆G we derived
in class to obtain an expression for the free energy barrier, ∆G(Rc).
"""

dG =



"""
(c) Numerically evaluate ∆G(Rc)/kT at 5 K below Tb, where Rc is already quite
small. Does this value seem reasonable? Again, be careful with units (is your ∆G
in Joules? Joules per mole? You will have to use consistent units for k).
"""





### PROBLEM 5 ###
"""
Consider the Dieterici equation of state,
P = N kT/(V − Nb) exp(−aN/(V kT)) 

(a) Locate (P, V, T) of the critical point. Definitely helpful to use Mathematica to
solve your simultaneous equations.
"""

k = c.k_B

def Dieterici_eos(P, V, T):
    p = (N*k*T)/(V - Nb) * np.exp(-a*N/(v*k*T))
    return p







# The End
