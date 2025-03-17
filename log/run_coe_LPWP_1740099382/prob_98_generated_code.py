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
    m = gp.Model("Vine Production")

    # Variables
    x = m.addVar(vtype=GRB.INTEGER, name="vintage_bottles")
    y = m.addVar(vtype=GRB.INTEGER, name="regular_bottles")

    # Constraints
    m.addConstr(500*x + 750*y <= 100000, "total_vine_constraint")
    m.addConstr(y >= 4*x + 10, "min_regular_bottles_constraint")
    m.addConstr(x >= 10, "min_vintage_bottles_constraint")

    # Objective
    m.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Optimize model
    m.optimize()

    return int(m.objVal)