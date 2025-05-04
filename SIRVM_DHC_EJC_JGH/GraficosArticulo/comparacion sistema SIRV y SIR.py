


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parámetros
beta = 0.0175
gamma = 0.005
v_list = [0.0, 0.0025, 0.005, 0.010]  # Tasa de vacunación tras t = 15
t_max = 2000
t_eval = np.linspace(0, t_max, 2000)
t_vac0 = 480  # Momento en que comienza la vacunación

S0 = 0.999
I0 = 1 - S0


def sirv(t, y, beta, gamma, v_post):
    S, I, R, V = y
    v = v_post if t > t_vac0 else 0  # Vacunación comienza en t > 15
    dSdt = -beta * S * I - v * S
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    dVdt = v * S
    return [dSdt, dIdt, dRdt, dVdt]

# Gráfica
plt.figure(figsize=(10, 6))

for v in v_list:
    sol = solve_ivp(sirv, [0, t_max], [S0, I0, 0, 0], args=(beta, gamma, v), t_eval=t_eval)
    plt.plot(sol.t, sol.y[1], label=f"$v = {v}$ desde $t = {t_vac0}$")

plt.xlabel("Tiempo (dias)")
plt.ylabel("Fracción Infectada $I(t)$")
plt.title("Modelo SIRV – Vacunación iniciada en $t = 480$")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
