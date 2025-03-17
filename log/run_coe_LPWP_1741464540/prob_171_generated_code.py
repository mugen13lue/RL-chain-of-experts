from scipy.optimize import linprog

def prob_171(regular_boats, speed_boats, regular_boat_capacity, regular_boat_gas,
              speed_boat_capacity, speed_boat_gas, max_regular_boat_trips,
              min_speed_boat_trips_percentage, mail_to_be_delivered): 
    """
    Args:
        regular_boats: an integer, number of regular boats
        speed_boats: an integer, number of speed boats
        regular_boat_capacity: an integer, number of mail pieces a regular boat can carry per trip
        regular_boat_gas: an integer, amount of gas (in liters) a regular boat uses per trip
        speed_boat_capacity: an integer, number of mail pieces a speed boat can carry per trip
        speed_boat_gas: an integer, amount of gas (in liters) a speed boat uses per trip
        max_regular_boat_trips: an integer, maximum number of trips a regular boat can make
        min_speed_boat_trips_percentage: a float, minimum percentage of trips that must be made by speed boats
        mail_to_be_delivered: an integer, number of mail pieces to be delivered
    
    Returns:
        objective_value: an integer, the minimum amount of gas consumed
    """
    c = [regular_boat_gas, speed_boat_gas]  # Coefficients of the objective function to minimize gas consumption
    A = [[-regular_boat_capacity, -speed_boat_capacity], [1, -0.5], [1, 1]]  # Coefficients of the constraints
    b = [-mail_to_be_delivered, 0, max_regular_boat_trips]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None), (0, None)])
    
    return res.fun