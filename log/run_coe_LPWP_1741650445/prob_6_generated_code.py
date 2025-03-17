from gurobipy import *

def prob_6(tomatoes, potatoes):
    """
    Args:
        tomatoes: an integer, representing the number of hectares of tomatoes to plant
        potatoes: an integer, representing the number of hectares of potatoes to plant
    Returns:
        obj: an integer, representing the maximum profit
    """
    m = Model("Farm_Profit")

    # Decision variables
    x = m.addVar(lb=20, vtype=GRB.CONTINUOUS, name="tomatoes")
    y = m.addVar(lb=30, vtype=GRB.CONTINUOUS, name="potatoes")

    # Objective function
    m.setObjective(350*x + 600*y, sense=GRB.MAXIMIZE)

    # Constraints
    m.addConstr(x + y <= 140, "total_hectares")
    m.addConstr(x >= 20, "tomatoes_constraint")
    m.addConstr(y >= 30, "potatoes_constraint")
    m.addConstr(x <= 2*y, "twice_tomatoes_to_potatoes")

    # Optimize model
    m.optimize()

    obj = int(m.objVal)

    return obj