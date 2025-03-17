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
    obj = 0
    
    # Create a new model
    model = gp.Model("ride_allocation")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of taxi rides
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of company car rides
    
    # Set objective: minimize the total number of taxi rides
    model.setObjective(x, GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(2*x + 3*y >= 500, "total_rides")
    model.addConstr(y <= 0.6*(x + y), "percentage_company_cars")
    model.addConstr(y >= 30, "min_company_car_rides")
    
    # Optimize model
    model.optimize()
    
    if model.status == GRB.OPTIMAL:
        obj = model.objVal
    
    return obj