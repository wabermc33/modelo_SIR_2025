from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Parámetros
beta_0 = 0.035/2
gamma = 0.01/2
S_0 = 0.999
n = 7        # Reducción de beta durante confinamiento
t_r = 90     # Duración del confinamiento

tc_list = [290, 440, 510, 650, 2000]  # Diferentes tiempos de inicio del confinamiento

t = np.linspace(0, 2000, 2000)

def vaccination_rate(t):
    return 0.007 if t >= 440 else 0

plt.figure(figsize=(10, 6))

# Iterar sobre distintos valores de t_c
for t_c in tc_list:

    # beta(t) depende del t_c actual
    def beta_t(t):
        if t < t_c:
            return beta_0
        elif t_c <= t < t_c + t_r:
            return beta_0 * (1/n)
        else:
            return beta_0

    def sirv(y, t, gamma):
        S, I, R, V = y
        v = vaccination_rate(t)
        beta = beta_t(t)
        dSdt = -beta * S * I - v * S
        dIdt = beta * S * I - gamma * I
        dRdt = gamma * I
        dVdt = v * S
        return [dSdt, dIdt, dRdt, dVdt]


    y0 = [S_0, 1 - S_0, 0, 0]
    sol = odeint(sirv, y0, t, args=(gamma,))

    # Graficar solo I(t)
    plt.plot(t, sol[:, 1], label=f't_c = {t_c}')


plt.title('Infectados I(t) para distintos inicios de confinamiento')
plt.xlabel('Tiempo (días)')
plt.ylabel('Proporción de infectados')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()