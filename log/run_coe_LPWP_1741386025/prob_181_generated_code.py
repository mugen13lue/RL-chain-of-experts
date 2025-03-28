import gurobipy as gp
from gurobipy import GRB

def prob_181(submarine, boat):
    """
    Args:
        submarine: an integer, number of submarine trips
        boat: an integer, number of boat trips
    Returns:
        obj: an integer, minimum amount of gas used
    """
    model = gp.Model("transportation")

    # Define variables
    x = model.addVar(vtype=GRB.INTEGER, name="submarine_trips")
    y = model.addVar(vtype=GRB.INTEGER, name="boat_trips")

    # Set objective
    model.setObjective(30*x + 25*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(100*x + 80*y >= 1000, "mail_constraint")
    model.addConstr(30*x + 25*y <= GRB.INFINITY, "gas_constraint")
    model.addConstr(x <= 6, "submarine_trips_constraint")
    model.addConstr(y >= 0.5*x, "boat_trips_constraint")

    # Optimize model
    model.optimize()

    # Get the minimum amount of gas used
    obj = model.objVal

    return obj