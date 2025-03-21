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
    m = gp.Model("ice_cream_production")

    # Variables
    x = m.addVar(lb=5, ub=10, vtype=GRB.INTEGER, name="chocolate_ice_cream")
    y = m.addVar(lb=5, ub=8, vtype=GRB.INTEGER, name="vanilla_ice_cream")

    # Constraints
    m.addConstr(x + 2*y <= 30, "hours_constraint")
    m.addConstr(x >= 6, "chocolate_workers_constraint")
    m.addConstr(y >= 2, "vanilla_workers_constraint")

    # Objective
    m.setObjective(200*x + 300*y, sense=GRB.MAXIMIZE)

    # Optimize model
    m.optimize()

    obj = m.objVal

    return obj