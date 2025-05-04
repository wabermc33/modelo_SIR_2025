import matplotlib.pyplot as plt

def print_graphics(simulation, cities, delta_t):
    for city in cities:
        datos = []
        citycode = cities.index(city)
        for tick in simulation:
            tickcode = simulation.index(tick)
            datos.append(simulation[tickcode][citycode][1])

        plt.plot(datos, marker='.', markersize=1)
        plt.title('') # f'{citycode}')
        plt.xlabel('Tiempo')
        plt.ylabel('Infectados')
        plt.ylim(top=11300)
        plt.grid(True)
        plt.savefig('grafica'+f'{citycode} .png', dpi=400)


