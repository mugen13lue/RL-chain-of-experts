from scipy.optimize import linprog

def prob_171(regular_boats, speed_boats, regular_boat_capacity, regular_boat_gas,
              speed_boat_capacity, speed_boat_gas, max_regular_boat_trips,
              min_speed_boat_trips_percentage, mail_to_be_delivered): 
    
    c = [regular_boat_gas, speed_boat_gas]
    A = [[-regular_boat_capacity, -speed_boat_capacity], [0, -0.5], [20, 30]]
    b = [-mail_to_be_delivered, 0, 1000]
    bounds = [(0, max_regular_boat_trips), (0, None)]
    
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    
    return res.fun