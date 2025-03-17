import gurobipy as gp
from gurobipy import GRB

def prob_9(carrots, cucumbers):
    """
    Args:
        carrots: an integer, the number of carrots sold each month
        cucumbers: an integer, the number of cucumbers sold each month

    Returns:
        obj: an integer, the maximum profit
    """
    model = gp.Model("profit_maximization")

    # Variables
    x = model.addVar(lb=300, ub=500, vtype=GRB.INTEGER, name="carrots")
    y = model.addVar(lb=0, ub=500, vtype=GRB.INTEGER, name="cucumbers")

    # Objective function
    model.setObjective(0.75*x + 0.8*y, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(0.3*x + 0.5*y <= 500, "budget_constraint")
    model.addConstr(y <= 1/3*x, "cucumbers_constraint")

    # Optimize model
    model.optimize()

    obj = model.objVal

    return obj