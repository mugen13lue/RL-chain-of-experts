import gurobipy as gp
from gurobipy import GRB

def prob_175(seasonal, full_time):
    """
    Args:
        seasonal: an integer (number of seasonal volunteers),
        full_time: an integer (number of full-time volunteers)
    Returns:
        obj: an integer (total number of gifts that can be delivered)
    """
    model = gp.Model("gift_delivery")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="seasonal")
    y = model.addVar(vtype=GRB.INTEGER, name="full_time")

    # Constraints
    model.addConstr(2*x + 5*y <= 200, "points_constraint")
    model.addConstr(x <= 0.3*(x+y), "seasonal_constraint")
    model.addConstr(y >= 10, "full_time_constraint")

    # Objective
    model.setObjective(5*x + 8*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)