import gurobipy as gp
from gurobipy import GRB

def prob_6(tomatoes, potatoes):
    """
    Args:
        tomatoes: an integer, representing the number of hectares of tomatoes to plant
        potatoes: an integer, representing the number of hectares of potatoes to plant
    Returns:
        obj: an integer, representing the maximum profit
    """
    m = gp.Model("crop_planting")

    # Decision variables
    x1 = m.addVar(lb=20, ub=140, vtype=GRB.CONTINUOUS, name="tomatoes")
    x2 = m.addVar(lb=30, ub=70, vtype=GRB.CONTINUOUS, name="potatoes")

    # Objective function
    m.setObjective(350*x1 + 600*x2, sense=GRB.MAXIMIZE)

    # Constraints
    m.addConstr(x1 <= 2*x2, "tomatoes_potatoes_ratio")
    m.addConstr(x1 + x2 <= 140, "total_hectares")
    
    m.optimize()

    return int(m.objVal)