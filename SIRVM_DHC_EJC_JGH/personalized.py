from input_functions import get_parameters, get_info, sim_time, vaccine_time

parameters = get_parameters()

cities = get_info()

delta_t = sim_time()

delta_t = 3600 * 24 # 84600

v_t = vaccine_time()


from city_functions import distance_calculate, flow_calculate, compute_simulation, first_tick

distance_map = distance_calculate(cities)

flows = flow_calculate(distance_map, cities)

tick_0 = first_tick(cities)

simulation = compute_simulation(cities, parameters, flows, tick_0, delta_t, v_t)

from graphic_functions import print_graphics

print_graphics(simulation, cities, delta_t)