from gurobipy import *

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
    m = Model("TaxiCompany")

    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="motorcycles")
    y = m.addVar(vtype=GRB.INTEGER, name="sedans")

    # Set objective function: Maximize 100x + 225y
    m.setObjective(100*x + 225*y, GRB.MAXIMIZE)

    # Add constraints
    m.addConstr(x <= 0.25*(x + y), "motorcycle_limit")
    m.addConstr(4*x + 15*y <= 200, "pollution_limit")
    m.addConstr(30*x + 70*y >= 1200, "transportation_limit")

    # Optimize the model
    m.optimize()

    # Get total earnings
    earnings = m.objVal

    return int(earnings)