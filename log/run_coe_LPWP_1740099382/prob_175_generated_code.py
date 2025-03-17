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
    seasonal_volunteers = model.addVar(vtype=GRB.INTEGER, name="seasonal_volunteers")
    full_time_volunteers = model.addVar(vtype=GRB.INTEGER, name="full_time_volunteers")

    # Constraints
    model.addConstr(2 * seasonal_volunteers + 5 * full_time_volunteers <= 200, "points_constraint")
    model.addConstr(seasonal_volunteers <= 0.3 * (seasonal_volunteers + full_time_volunteers), "seasonal_constraint")
    model.addConstr(full_time_volunteers >= 10, "full_time_constraint")

    # Objective
    model.setObjective(5 * seasonal_volunteers + 8 * full_time_volunteers, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)