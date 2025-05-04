from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


beta_0 = 0.0175
gamma = 0.005
m = 0.0007
S_0 = 0.999
t_v = 480


# Confinament
t_c = 300   # temps d'inici
t_r = 90  # duració
n = 7       # grau de reducció de beta

# Funció beta(t)
def beta_t(t):
    if t < t_c:
        return beta_0
    elif t_c <= t < t_c + t_r:
        return beta_0 / n
    else:
        return beta_0

# Vacunació
def vaccination_rate(t):
    return 0.0025 if t >= t_v else 0

# Model SIRV amb morts i beta(t)
def sirv_confinamiento(y, t, gamma, m):
    S, I, R, V, M = y
    b = beta_t(t)
    v = vaccination_rate(t)
    dSdt = -b * S * I - v * S
    dIdt = b * S * I - gamma * I - m * I
    dRdt = gamma * I
    dVdt = v * S
    dMdt = m * I
    return [dSdt, dIdt, dRdt, dVdt, dMdt]

# Condicions inicials i temps
y0 = [S_0, 1 - S_0, 0.0, 0.0, 0.0]
t = np.linspace(0, 2000, 1000)

# Simulació
sol = odeint(sirv_confinamiento, y0, t, args=(gamma, m))

# Gràfiques
plt.plot(t, sol[:, 0], label='S (Susceptibles)')
plt.plot(t, sol[:, 1], label='I (Infectats)')
plt.plot(t, sol[:, 2], label='R (Recuperats)')
plt.plot(t, sol[:, 3], label='V (Vacunats)')
plt.plot(t, sol[:, 4], label='M (Morts acumulades)')
plt.axvspan(t_c, t_c + t_r, color='gray', alpha=0.2, label='Confinament')
plt.xlabel('Temps')
plt.ylabel('Proporcions')
plt.title('Model SIRV amb confinament i vacunació')
plt.legend()
plt.grid(True)
plt.show()

# Mostrar morts totals
print(f"Total de morts: {sol[-1, 4]:.4f}")