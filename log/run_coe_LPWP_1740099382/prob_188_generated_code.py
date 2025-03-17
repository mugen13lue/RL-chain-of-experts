import gurobipy as gp
from gurobipy import GRB

def prob_188(taxis, company_cars):
    """
    Args:
        taxis: an integer, number of taxi rides
        company_cars: an integer, number of company car rides
    
    Returns:
        obj: an integer, minimized total number of taxi rides
    """
    model = gp.Model("ride_allocation")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of taxi rides
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of company car rides

    # Constraints
    model.addConstr(2*x + 3*y >= 500, "total_rides")
    model.addConstr(y <= 0.6*(x + y), "percentage_company_cars")
    model.addConstr(y >= 30, "min_company_car_rides")

    # Objective
    model.setObjective(x, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)  # Return the minimized total number of taxi rides