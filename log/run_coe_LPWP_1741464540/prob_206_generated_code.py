import gurobipy as gp
from gurobipy import GRB

def prob_206():
    """
    Returns:
        obj: an integer representing the maximum profit
    """
    model = gp.Model("toy_store")

    # Variables
    x = model.addVar(lb=90, ub=190, vtype=GRB.INTEGER, name="plush_toys")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="dolls")

    # Constraints
    model.addConstr(3*x + 2*y <= 700, "budget_constraint")
    model.addConstr(y <= 2*x, "doll_sales_constraint")

    # Objective
    model.setObjective(4*x + 2*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)