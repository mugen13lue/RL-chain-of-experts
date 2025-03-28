import gurobipy as gp
from gurobipy import GRB

def prob_146():
    """
    Returns:
        sugar_intake: an integer, the minimum sugar intake
    """
    model = gp.Model("diet_problem")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="blueberries")
    y = model.addVar(vtype=GRB.INTEGER, name="strawberries")

    # Constraints
    model.addConstr(3*x + y >= 90, "anti-oxidants")
    model.addConstr(5*x + 7*y >= 100, "minerals")
    model.addConstr(y >= 3*x, "strawberry_ratio")

    # Objective
    model.setObjective(5*x + 7*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    sugar_intake = model.objVal

    return sugar_intake