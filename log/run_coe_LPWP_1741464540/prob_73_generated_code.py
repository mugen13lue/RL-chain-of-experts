import gurobipy as gp
from gurobipy import GRB

def prob_73(regular, hybrid):
    """
    Args:
        regular: an integer, number of regular vans
        hybrid: an integer, number of hybrid vans
    Returns:
        obj: an integer, total number of vans
    """
    model = gp.Model("van_purchase")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="regular_vans")
    y = model.addVar(vtype=GRB.INTEGER, name="hybrid_vans")

    # Constraints
    model.addConstr(500*x + 300*y >= 20000, "packages_constraint")
    model.addConstr(200*x + 100*y <= 7000, "pollutants_constraint")

    # Objective
    model.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Get the total number of vans
    obj = model.objVal

    return obj