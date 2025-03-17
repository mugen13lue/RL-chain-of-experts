import gurobipy as gp
from gurobipy import GRB

def prob_98(vintage_bottles, regular_bottles):
    """
    Args:
        vintage_bottles: an integer (number of vintage bottles)
        regular_bottles: an integer (number of regular bottles)
    Returns:
        obj: an integer (maximum total number of bottles produced)
    """
    # Create a new model
    model = gp.Model("vine_production")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="vintage_bottles")
    y = model.addVar(vtype=GRB.INTEGER, name="regular_bottles")

    # Constants
    V_vintage = 500
    V_regular = 750
    V_total = 100000
    min_vintage = 10
    min_regular = 4 * min_vintage

    # Objective: maximize total number of bottles produced
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(V_vintage * x + V_regular * y <= V_total, "total_volume_constraint")
    model.addConstr(y >= 4 * x, "regular_vintage_ratio_constraint")
    model.addConstr(x >= min_vintage, "min_vintage_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj