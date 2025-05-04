import math

def distance_calculate(cities):
    current_city = 0
    n_cities = len(cities)
    distance_map = []
    while current_city < n_cities:
        distances = ()
        x = cities[current_city][0]
        y = cities[current_city][1]
        for city in cities:
            d = math.sqrt((x-city[0])**2 + (y-city[1])**2)
            distances += (d,)
        distance_map.append(distances)
        current_city += 1
    return distance_map


def flow_calculate(distance_map, cities):
    cities_population = []

    for city in cities:
        cities_population.append(city[2])

    cities_denominators = []
    for city in distance_map:
        denominator = 0
        i = distance_map.index(city)
        for d in city:
            e = city.index(d)
            if i == e:
                continue
            else:
                denominator += cities_population[e]/d
        cities_denominators.append(denominator)

    temp_flows = []
    for city in distance_map:
        i = distance_map.index(city)
        temp_flow_city = ()
        for d in city:
            e = city.index(d)
            if e == i:
                temp_flow_city += (0,)
                continue
            else:
                temp_flow_city += ((cities_population[e]/d)/cities_denominators[i],)
        temp_flows.append(temp_flow_city)

    flows = []
    for city in temp_flows:
        i = temp_flows.index(city)
        flow_city = ()
        for flow in city:
            e = city.index(flow)
            if e == i:
                flow_city += (0,)
                continue
            else:
                N_a = cities_population[i]
                N_b = cities_population[e]
                exit_a = cities[i][3]/100
                exit_b = cities[e][3]/100
                flow_ab = temp_flows[i][e]
                flow_ba = temp_flows[e][i]
                flow_city += (N_a * exit_a * flow_ab + N_b * exit_b * flow_ba,)
        flows.append(flow_city)

    return flows

def first_tick(cities):
    tick_0 = []
    for city in cities:
        susceptible = city[2] - city[4]
        infected = city[4]
        recovered = 0
        vaccinated = 0
        dead = 0
        city_0 = (susceptible, infected, recovered, vaccinated, dead)
        tick_0.append(city_0)
    return tick_0

def compute_simulation(cities, parameters, flows, tick_0, sim_time, v_t):
    v_time = v_t * 86400
    time = 0
    simulation = []
    current_SIRVM = tick_0
    c  = sim_time / 86400
    beta = parameters[0] * c
    gamma = parameters[1] * c
    v = parameters[2] * c
    m = parameters[3] * c
    dead = 0

    while True:
        temp_SIRVM = []
        total_infected = 0
        for city in current_SIRVM:
            total_infected += city[1]
        if total_infected < 1:
            break
        for city in current_SIRVM:
            city_code = current_SIRVM.index(city)
            new_susceptible = 0
            new_infected = 0
            new_recovered = 0
            new_vaccinated = 0
            for outgoing_flows in flows:
                external_city_code = flows.index(outgoing_flows)

                new_susceptible += outgoing_flows[city_code] * c * (current_SIRVM[external_city_code][0]/cities[external_city_code][2])
                new_infected += outgoing_flows[city_code]* c * (current_SIRVM[external_city_code][1]/cities[external_city_code][2])
                new_recovered += outgoing_flows[city_code] * c * (current_SIRVM[external_city_code][2]/cities[external_city_code][2])
                new_vaccinated += outgoing_flows[city_code] * c * (current_SIRVM[external_city_code][3]/cities[external_city_code][2])

            total_new_people = new_susceptible + new_infected + new_recovered + new_vaccinated
            increase_factor = 1 + (total_new_people/cities[city_code][2])

            susceptible = (city[0] + new_susceptible)/increase_factor
            infected = (city[1] + new_infected)/increase_factor
            recovered = (city[2] + new_recovered)/increase_factor
            vaccinated = (city[3] + new_vaccinated)/increase_factor

            next_susceptible = susceptible - (beta * susceptible * infected)/cities[city_code][2]
            next_infected = infected + (beta * susceptible * infected)/cities[city_code][2] - ((gamma) * infected)
            next_recovered = recovered + (gamma * infected)

            if time > v_time:
                next_vaccinated = vaccinated + v * susceptible
                next_susceptible += -(v * susceptible)
            else:
                next_vaccinated = 0

            temp_SIRVM.append([next_susceptible, next_infected, next_recovered, next_vaccinated, dead])

        for city in current_SIRVM:
            city_code = current_SIRVM.index(city)
            inf = temp_SIRVM[city_code][1]
            temp_SIRVM[city_code][1] = (1-m) * temp_SIRVM[city_code][1]
            dead += m * inf

        time += sim_time
        simulation.append(temp_SIRVM)
        current_SIRVM = temp_SIRVM

    return simulation
























