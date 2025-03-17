from gurobipy import *

def prob_8(clothing_company, tech_company):
    """
    Args:
        clothing_company: an integer, representing the investment in the clothing company.
        tech_company: an integer, representing the investment in the tech company.
    Returns:
        obj: an integer, representing the maximum profit.
    """
    m = Model("investment")

    # Variables
    x = m.addVar(lb=0, vtype=GRB.CONTINUOUS, name="clothing_company")
    y = m.addVar(lb=0, ub=500, vtype=GRB.CONTINUOUS, name="tech_company")

    # Constraints
    m.addConstr(x + y <= 3000, "investment_amount")
    m.addConstr(x >= 4*y, "minimum_investment_ratio")

    # Objective
    m.setObjective(0.07*x + 0.10*y, GRB.MAXIMIZE)

    m.optimize()

    obj = m.objVal

    return obj