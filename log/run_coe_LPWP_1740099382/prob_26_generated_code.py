import gurobipy as gp
from gurobipy import GRB

def prob_26(Zodiac, Sunny):
    """
    Args:
        Zodiac: an integer, number of pills of Zodiac
        Sunny: an integer, number of pills of Sunny
    Returns:
        obj: an integer, objective value
    """
    model = gp.Model("medicine_optimization")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of pills of Zodiac
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of pills of Sunny

    # Constraints
    model.addConstr(1.3*x + 1.2*y >= 5, "Z1_Requirement")
    model.addConstr(1.5*x + 5*y >= 10, "D3_Requirement")

    # Objective
    model.setObjective(x + 3*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    obj = model.objVal

    return obj