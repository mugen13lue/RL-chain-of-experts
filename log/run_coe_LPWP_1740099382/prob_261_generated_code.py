import gurobipy as gp
from gurobipy import GRB

def prob_261(motorcycles, sedans, constraint1, constraint2, constraint3):
    """
    Args:
        motorcycles: an integer, number of motorcycles
        sedans: an integer, number of sedans
        constraint1: a boolean, whether the motorcycle limit is satisfied
        constraint2: a boolean, whether the pollution limit is satisfied
        constraint3: a boolean, whether the transportation limit is satisfied
    Returns:
        obj: an integer, total earnings
    """
    
    # Create a new model
    model = gp.Model("taxi_company")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="motorcycles")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="sedans")

    # Set objective function
    model.setObjective(100*x + 225*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x <= 0.25*(x + y))
    model.addConstr(4*x + 15*y <= 200)
    model.addConstr(30*x + 70*y >= 1200)

    # Optimize model
    model.optimize()

    # Get the total earnings
    obj = model.objVal

    return obj