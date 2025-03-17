from gurobipy import *

def prob_8():
    m = Model("investment")

    # Variables
    x = m.addVar(lb=0, vtype=GRB.CONTINUOUS, name="clothing_company_investment")
    y = m.addVar(lb=0, ub=500, vtype=GRB.CONTINUOUS, name="tech_company_investment")

    # Constraints
    m.addConstr(x + y <= 3000, "investment_amount")
    m.addConstr(x >= 4*y, "minimum_investment_ratio")
    m.addConstr(y <= 500, "tech_company_limit")

    # Objective
    m.setObjective(0.07*x + 0.10*y, GRB.MAXIMIZE)

    m.optimize()

    obj = m.objVal

    return obj