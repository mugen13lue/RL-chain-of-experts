import gurobipy as gp
from gurobipy import GRB

def prob_227(subsoil, topsoil):
    """
    Args:
        subsoil: an integer, number of bags of subsoil
        topsoil: an integer, number of bags of topsoil

    Returns:
        obj: an integer, the minimized amount of water required to hydrate the garden bed
    """
    obj = 1e9

    # Create a new model
    model = gp.Model("minimize_water")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="subsoil")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="topsoil")

    # Set objective function
    model.setObjective(10*x + 6*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(10*x + 6*y <= 150, "water_constraint")
    model.addConstr(y >= 10, "min_topsoil_constraint")
    model.addConstr(y <= 0.3*(x + y), "topsoil_percentage_constraint")

    # Optimize the model
    model.optimize()

    if model.status == GRB.OPTIMAL:
        obj = model.objVal

    return obj