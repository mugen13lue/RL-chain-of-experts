from gurobipy import *

def prob_25(apartments, townhouses):
    """
    
    Args:
        apartments: an integer, amount of money invested in apartments
        townhouses: an integer, amount of money invested in townhouses
    
    Returns:
        profit: an integer, maximum profit
    """
    m = Model("investment")

    # Decision variables
    x = m.addVar(vtype=GRB.CONTINUOUS, name="apartments")
    y = m.addVar(vtype=GRB.CONTINUOUS, name="townhouses")

    # Objective function
    m.setObjective(0.10*x + 0.15*y, GRB.MAXIMIZE)

    # Constraints
    m.addConstr(x + y <= 600000)
    m.addConstr(x <= 200000)
    m.addConstr(x >= 0.5*y)
    m.addConstr(x >= 0)
    m.addConstr(y >= 0)

    m.optimize()

    return int(m.objVal)