from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Parámetros a modificar
beta = 0.032
gamma = 0.02
I_0=0.6
S_0=1-I_0

# Ecuaciones SIR
def sir(y, t, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    
    return [dSdt, dIdt, dRdt]

y0 = [S_0, I_0, 0.0]
t = np.linspace(0, 2000, 3000)
sol = odeint(sir, y0, t, args=(beta, gamma)) 
#La función odeint() lo que hace es calcular las derivadas de S, I, R, para calcular
#sus valores en el siguiente t y poder después gráficar por ejemplo. Y grácias a args
#podemos tener beta y gamma como parametros adicionales a usar.

# Gráfica
plt.plot(t, sol[:,0], label='S')
plt.plot(t, sol[:,1], label='I')
plt.plot(t, sol[:,2], label='R')
plt.legend()
plt.xlabel('Tiempo (dias)')
plt.ylabel('Proporciones')
plt.title('Modelo SIR')
plt.grid(True) 
plt.show()  