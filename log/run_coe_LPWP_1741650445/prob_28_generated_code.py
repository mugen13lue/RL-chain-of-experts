import gurobipy as gp
from gurobipy import GRB

def prob_28(phones, laptops):
    """
    Args:
        phones: an integer, number of phones
        laptops: an integer, number of laptops
    Returns:
        obj: an integer, maximum profit
    """
    m = gp.Model("inventory_optimization")

    # Variables
    x = m.addVar(vtype=GRB.INTEGER, name="phones")
    y = m.addVar(vtype=GRB.INTEGER, name="laptops")

    # Constraints
    m.addConstr(x + 4*y <= 400, "floor_space_constraint")
    m.addConstr(y >= 0.8*(x + y), "appliances_stock_constraint")
    m.addConstr(400*x + 100*y <= 6000, "cost_constraint")
    m.addConstr(x >= 0, "non_negativity_constraint_phones")
    m.addConstr(y >= 0, "non_negativity_constraint_laptops")

    # Objective
    m.setObjective(120*x + 40*y, sense=GRB.MAXIMIZE)

    # Optimize model
    m.optimize()

    return int(m.objVal) if m.status == GRB.OPTIMAL else None