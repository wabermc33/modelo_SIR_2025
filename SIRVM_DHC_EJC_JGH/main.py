from input_functions import get_parameters, get_info, sim_time, vaccine_time

# parameters = get_parameters()
parameters = (0.35, 0.1, 0.01, 0.001)

cities = [
    [1812, 4484, 10000, 1, 1],
    [2344, 4518, 5000, 1, 0],
    [2014, 4013, 8000, 1, 0],
    [2300, 4040, 20000, 1, 0],
    [2752, 4048, 30000, 1, 0],
    [3200, 3900, 4000, 1, 0],
    [1790, 3800, 5000, 1, 0],
    [2030, 3700, 7000, 1, 0],
    [2300, 3675, 11000, 1, 0],
    [1650, 3660, 3000, 1, 0],
    [1824, 3560, 1000, 1, 0],
    [2000, 3500, 4000, 1, 0],
    [1724, 3478, 1000, 1, 0],
    [1370, 3382, 2000, 1, 0],
    [2516, 3452, 20000, 1, 0],
    [3130, 3240, 2000, 1, 0],
    [1300, 3000, 3000, 1, 0],
    [1021, 2930, 2000, 1, 0],
    [2280, 2949, 9000, 1, 0],
    [1413, 2626, 3000, 1, 0],
    [1714, 2659, 1000, 1, 0],
    [2016, 2469, 1000, 1, 0],
    [3500, 2100, 5000, 1, 0],
    [1406, 2364, 4000, 1, 0],
    [2685, 2322, 10000, 1, 0],
    [1945, 1965, 1000, 1, 0],
    [3154, 1891, 9000, 1, 0],
    [2651, 1747, 100, 1, 0],
    [1334, 1700, 1000, 1, 0],
    [1809, 1647, 500, 1, 0],
    [3154, 1417, 5000, 1, 0],
    [1566, 1197, 50, 1, 0],
    [1843, 1381, 500, 1, 0],
    [2103, 1083, 1000, 1, 0],
    [2644, 1161, 2000, 1, 0],
    [3241, 1008, 300, 1, 0],
    [3417, 999, 500, 1, 0],
    [2227, 730, 6000, 1, 0],
    [2689, 715, 1000, 1, 0],
]


# delta_t = sim_time()
delta_t = 3600 * 24 # 84600

# v_t = vaccine_time()
v_t = 43

from city_functions import distance_calculate, flow_calculate, compute_simulation, first_tick

distance_map = distance_calculate(cities)

flows = flow_calculate(distance_map, cities)

tick_0 = first_tick(cities)

simulation = compute_simulation(cities, parameters, flows, tick_0, delta_t, v_t)

from graphic_functions import print_graphics

print_graphics(simulation, cities, delta_t)













