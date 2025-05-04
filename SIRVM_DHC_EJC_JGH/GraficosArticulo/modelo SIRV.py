from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


beta = 0.0175
gamma = 0.005
S_0=0.999

def vaccination_rate(t):
    return 0.006 if t >= 480 else 0


def sirv(y, t, beta, gamma):
    S, I, R, V = y
    v = vaccination_rate(t)
    dSdt = -beta * S * I - v * S
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    dVdt = v * S
    return [dSdt, dIdt, dRdt, dVdt]


y0 = [S_0, 1-S_0, 0, 0]
t = np.linspace(0, 2000, 1000)  

sol = odeint(sirv, y0, t, args=(beta, gamma))

plt.plot(t, sol[:, 0], label='S')
plt.plot(t, sol[:, 1], label='I')
plt.plot(t, sol[:, 2], label='R')
plt.plot(t, sol[:, 3], label='V')
plt.legend()
plt.xlabel('Tiempo (dias)')
plt.ylabel('Proporciones')
plt.title('Modelo SIRV')
plt.grid(True)
plt.show()