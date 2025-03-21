import gurobipy as gp
from gurobipy import GRB

def prob_131(bananas, mangoes):
    """
    Args:
        bananas: an integer, number of bananas
        mangoes: an integer, number of mangoes
    Returns:
        obj: an integer, minimum sugar intake
    """
    model = gp.Model("GorillaDiet")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="bananas")
    y = model.addVar(vtype=GRB.INTEGER, name="mangoes")

    # Constraints
    model.addConstr(80*x + 100*y >= 4000)
    model.addConstr(20*x + 15*y >= 150)
    model.addConstr(10*x + 8*y <= 0.33*(10*x + 8*y))

    # Objective
    model.setObjective(10*x + 8*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)