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

    # Decision variables
    x = m.addVar(vtype=GRB.CONTINUOUS, name="clothing_company_investment")
    y = m.addVar(vtype=GRB.CONTINUOUS, name="tech_company_investment")

    # Objective function
    m.setObjective(0.07 * x + 0.10 * y, sense=GRB.MAXIMIZE)

    # Constraints
    m.addConstr(x + y <= 3000, "investment_amount")
    m.addConstr(x >= 4 * y, "min_investment_clothing")
    m.addConstr(y <= 500, "max_investment_tech")

    m.optimize()

    obj = m.objVal

    return obj