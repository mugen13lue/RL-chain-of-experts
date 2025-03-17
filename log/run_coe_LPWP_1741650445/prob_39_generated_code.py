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
    # Create a new model
    model = gp.Model("ice_cream_production")

    # Decision variables
    x = model.addVar(lb=5, ub=10, vtype=GRB.INTEGER, name="chocolate_ice_cream")
    y = model.addVar(lb=5, ub=8, vtype=GRB.INTEGER, name="vanilla_ice_cream")

    # Objective function: Maximize profit
    model.setObjective(200*x + 300*y, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(x + 2*y <= 30, "production_time_constraint")
    model.addConstr(x >= 6, "chocolate_workers_constraint")
    model.addConstr(y >= 2, "vanilla_workers_constraint")

    # Optimize the model
    model.optimize()

    # Get the maximum profit
    obj = model.objVal

    return obj