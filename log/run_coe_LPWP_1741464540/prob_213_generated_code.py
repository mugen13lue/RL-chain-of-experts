import gurobipy as gp
from gurobipy import GRB

def prob_213():
    """
    Returns:
        profit (int): Maximum monthly profit
    """
    model = gp.Model("handbags")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="regular_handbags")
    y = model.addVar(vtype=GRB.INTEGER, name="premium_handbags")

    # Constraints
    model.addConstr(200*x + 447*y <= 250000, "budget_constraint")
    model.addConstr(x <= 475, "regular_handbags_constraint")
    model.addConstr(y <= 475, "premium_handbags_constraint")

    # Objective
    model.setObjective(30*x + 180*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)