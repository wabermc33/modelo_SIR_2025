from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Parámetros a modificar
beta = 0.0175
gamma = 0.005
m=0.0001
I_0=0.001
S_0=1-I_0

# Ecuaciones SIR con muertes
def sir_con_muertes(y, t, beta, gamma, m):
    S, I, R, M = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I -m *I
    dRdt = gamma * I
    dMdt = m * I
    return [dSdt, dIdt, dRdt, dMdt]

y0 = [S_0, I_0, 0.000, 0.000]
t = np.linspace(0, 2000, 3000)
sol = odeint(sir_con_muertes, y0, t, args=(beta, gamma, m)) 

plt.plot(t, sol[:, 0], label='S (Susceptibles)')
plt.plot(t, sol[:, 1], label='I (Infectados)')
plt.plot(t, sol[:, 2], label='R (Recuperados)')
plt.plot(t, sol[:, 3], label='M (Muertes acumuladas)')
plt.xlabel('Tiempo')
plt.ylabel('Proporciones')
plt.title('Modelo SIR con muertes')
plt.legend()
plt.grid(True)
plt.show()

muertes_totales = sol[-1, 3] 

print(f'Número total de muertes: {muertes_totales:.5f}')