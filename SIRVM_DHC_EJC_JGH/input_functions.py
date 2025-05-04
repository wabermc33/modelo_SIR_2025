def get_info():
    keep_asking = True
    cities = []
    while keep_asking == True:
        x = float(input("Coordenadas x de la ciudad: "))
        y = float(input("Coordenadas y de la ciudad: "))
        population = int(input("Población de la ciudad: "))
        flow = float(input("Porcentaje de población que sale de la ciudad diariamente (e.g. 5.2): "))
        infected_day_0 = int(input('Número de infectados en el día 0: '))
        city = [x,y,population,flow,infected_day_0]
        cities.append(city)
        while True:
            choice = input("Agregar otra ciudad (Y/N)?: ")
            if choice == "Y" or choice == "y":
                break
            elif choice == "N" or choice == "n":
                keep_asking = False
                break
            else:
                print("Entrada errónea.")
    return cities

def get_parameters():
    parameters = ()
    while True:
        beta = float(input('Introduzca una beta: '))
        if beta < 0 or beta > 1:
            continue
        else:
            parameters += (beta,)
            break
    while True:
        gamma = float(input('Introduzca una gamma: '))
        if gamma < 0 or gamma > 1:
            continue
        else:
            parameters += (gamma,)
            break
    while True:
        v = float(input('Introduzca una v: '))
        if v < 0 or v > 1:
            continue
        else:
            parameters += (v,)
            break
    while True:
        m = float(input('Introduzca una m: '))
        if m < 0 or m > 1:
            continue
        else:
            parameters += (m,)
            break
    return parameters

def sim_time():
    delta_t = float(input('Introduzca el mínimo intérvalo de tiempo de la simulación (en segundos): '))
    return delta_t

def vaccine_time():
    v_t = float(input('Introduzca el tiempo (en días) para la aparición de la vacuna: '))
    return v_t
