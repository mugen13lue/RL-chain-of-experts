def prob_172(bus, car):
    """
    Args:
        bus: an integer
        car: an integer
    Returns:
        obj: an integer
    """
    from scipy.optimize import minimize

    def objective_function(x):
        bus_trips = x[0]
        car_trips = x[1]
        total_time = bus_trips*2 + car_trips*1.5
        return total_time

    def constraint1(x):
        return x[0]*100 + x[1]*40 - 1200

    def constraint2(x):
        return x[0] - 10

    def constraint3(x):
        return x[1] - 0.6*(x[0]+x[1])

    x0 = [5, 5]  # initial guess

    # define the bounds for the variables
    bounds = ((0, 10), (0, 10))

    # define the constraints
    cons = [{'type': 'eq', 'fun': constraint1},
            {'type': 'ineq', 'fun': constraint2},
            {'type': 'ineq', 'fun': constraint3}]

    # minimize the objective function with the defined constraints
    result = minimize(objective_function, x0, bounds=bounds, constraints=cons)

    return result.fun

# Test the function with the given problem
print(prob_172(100, 40))  # Output should be the minimum total time needed to transport the chicken