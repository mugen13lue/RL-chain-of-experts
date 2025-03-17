import gurobipy as gp
from gurobipy import GRB

def prob_188(taxis, company_cars):
    """
    Args:
        taxis: an integer, number of taxi rides
        company_cars: an integer, number of company car rides
    
    Returns:
        taxi_rides: an integer, number of taxi rides to minimize
        car_rides: an integer, number of company car rides to minimize
    """
    m = gp.Model("ride_allocation")

    # Decision variables
    taxi_rides = m.addVar(vtype=GRB.INTEGER, name="taxi_rides")
    car_rides = m.addVar(vtype=GRB.INTEGER, name="car_rides")

    # Objective function: minimize total number of taxi rides
    m.setObjective(taxi_rides, GRB.MINIMIZE)

    # Constraints
    m.addConstr(2 * taxi_rides + 3 * car_rides >= 500, "total_employees")
    m.addConstr(car_rides <= 0.6 * (taxi_rides + car_rides), "max_car_rides")
    m.addConstr(car_rides >= 30, "min_car_rides")

    # Optimize model
    m.optimize()

    return int(taxi_rides.x) if m.status == GRB.OPTIMAL else None, int(car_rides.x) if m.status == GRB.OPTIMAL else None