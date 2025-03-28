from gurobipy import *

def prob_6(tomatoes, potatoes):
    """
    Args:
        tomatoes: an integer, representing the number of hectares of tomatoes to plant
        potatoes: an integer, representing the number of hectares of potatoes to plant
    Returns:
        obj: an integer, representing the maximum profit
    """
    m = Model()

    # Variables
    x = m.addVar(lb=20, ub=140, vtype=GRB.CONTINUOUS, name="tomatoes")
    y = m.addVar(lb=30, ub=110, vtype=GRB.CONTINUOUS, name="potatoes")

    # Objective Function
    m.setObjective(350*x + 600*y, sense=GRB.MAXIMIZE)

    # Constraints
    m.addConstr(x + y <= 140)
    m.addConstr(x >= 20)
    m.addConstr(y >= 30)
    m.addConstr(x <= 2*y)

    m.optimize()

    obj = m.objVal

    return obj