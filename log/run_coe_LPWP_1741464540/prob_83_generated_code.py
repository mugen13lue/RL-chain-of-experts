import gurobipy as gp
from gurobipy import GRB

def prob_83(var_4wheeler, var_3wheeler):
    """
    Args:
        var_4wheeler: an integer, number of 4-wheeler vehicles
        var_3wheeler: an integer, number of 3-wheeler vehicles
    Returns:
        obj: an integer, objective value
    """
    model = gp.Model("vehicle_optimization")

    # Decision variables
    x = model.addVar(vtype=GRB.CONTINUOUS, name="x")
    y = model.addVar(vtype=GRB.CONTINUOUS, name="y")

    # Set objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(60*x + 40*y >= 1000, "luggage_constraint")
    model.addConstr(30*x + 15*y <= 430, "pollutant_constraint")

    # Optimize model
    model.optimize()

    # Get objective value
    obj = model.objVal

    return obj