from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

beta = 0.0175
gamma = 0.005
S_0 = 0.999
I_0 = 1 - S_0

# Lista de tiempos de inicio de vacunación
t_v_list = [365, 480, 730 , 2000]

# Tiempo total de simulación
t = np.linspace(0, 2000, 2000)

def make_vaccination_rate(t_v):
    def vaccination_rate(t):
        return 0.006 if t >= t_v else 0
    return vaccination_rate

def sirv(y, t, beta, gamma, vaccination_rate):
    S, I, R, V = y
    v = vaccination_rate(t)
    dSdt = -beta * S * I - v * S
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    dVdt = v * S
    return [dSdt, dIdt, dRdt, dVdt]

plt.figure(figsize=(10, 6))

for t_v in t_v_list:
    vacc_rate_func = make_vaccination_rate(t_v)
    sol = odeint(sirv, [S_0, I_0, 0, 0], t, args=(beta, gamma, vacc_rate_func))
    plt.plot(t, sol[:, 1], label=f"t_v = {t_v}")

plt.xlabel("Tiempo (dias)")
plt.ylabel("Fracción infectada I(t)")
plt.title("Comparación de I(t) para distintos inicios de vacunación")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()