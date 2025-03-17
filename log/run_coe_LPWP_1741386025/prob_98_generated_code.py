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
    model = gp.Model("bottle_production")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="vintage_bottles")
    y = model.addVar(vtype=GRB.INTEGER, name="regular_bottles")

    # Constraints
    model.addConstr(500*x + 750*y <= 100000, "total_vine_constraint")
    model.addConstr(y >= 4*x, "regular_bottles_constraint")
    model.addConstr(x >= 10, "minimum_vintage_bottles_constraint")

    # Objective
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)