import gurobipy as gp
from gurobipy import GRB

def prob_5(telecom, healthcare, three, _3, _1):
    """
    Args:
        telecom: an integer, amount invested in telecom
        healthcare: an integer, amount invested in healthcare
        three: an integer, constraint parameter
        _3: a float, telecom investment percentage
        _1: a float, healthcare investment percentage
    Returns:
        profit: a float, maximum profit
    """
    m = gp.Model("investment")

    # Variables
    x = m.addVar(lb=0, vtype=GRB.CONTINUOUS, name="healthcare")
    y = m.addVar(lb=0, ub=70000, vtype=GRB.CONTINUOUS, name="telecom")

    # Constraints
    m.addConstr(x <= y / three, "healthcare_constraint")
    m.addConstr(y <= 70000, "telecom_constraint")
    m.addConstr(x + y <= 100000, "total_investment_constraint")

    # Objective
    m.setObjective(_1 * x + _3 * y, GRB.MAXIMIZE)

    m.optimize()

    return m.objVal