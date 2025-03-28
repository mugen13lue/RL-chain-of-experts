import gurobipy as gp
from gurobipy import GRB

def prob_173():
    """
    Returns:
        obj: an integer, the total amount of pollution produced
    """
    model = gp.Model("pollution_minimization")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of vans used
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of minibuses used

    # Constraints
    model.addConstr(6*x + 10*y >= 150, "num_kids_constraint")
    model.addConstr(y <= 10, "num_minibuses_constraint")
    model.addConstr(x >= y, "num_vans_constraint")

    # Objective
    model.setObjective(7*x + 10*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Get the total amount of pollution produced
    obj = model.objVal

    return obj