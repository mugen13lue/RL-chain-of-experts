import gurobipy as gp
from gurobipy import GRB

def prob_39(chocolate_ice_cream, vanilla_ice_cream):
    """
    Args:
        chocolate_ice_cream: an integer, the number of gallons of chocolate ice cream
        vanilla_ice_cream: an integer, the number of gallons of vanilla ice cream
    Returns:
        obj: an integer, the maximum profit
    """
    model = gp.Model("ice_cream_production")

    # Variables
    x = model.addVar(lb=5, ub=10, vtype=GRB.INTEGER, name="chocolate_ice_cream")
    y = model.addVar(lb=5, ub=8, vtype=GRB.INTEGER, name="vanilla_ice_cream")

    # Constraints
    model.addConstr(x + 2*y <= 30, "production_time")
    model.addConstr(x >= 1, "worker_requirement_chocolate")
    model.addConstr(2*y >= 6, "worker_requirement_vanilla")

    # Objective
    model.setObjective(200*x + 300*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)