from gurobipy import *

def prob_146(blueberries, strawberries):
    """
    Args:
        blueberries: an integer, the number of packs of blueberries
        strawberries: an integer, the number of packs of strawberries
    Returns:
        sugar_intake: an integer, the minimum sugar intake
    """
    model = Model("diet_problem")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="blueberries")
    y = model.addVar(vtype=GRB.INTEGER, name="strawberries")

    # Objective function: minimize sugar intake
    model.setObjective(5*x + 7*y, GRB.MINIMIZE)

    # Constraints
    model.addConstr(3*x + y >= 90, "anti-oxidants")
    model.addConstr(5*x + 7*y >= 100, "minerals")
    model.addConstr(y >= 3*x, "strawberries_blueberries_ratio")

    # Optimize model
    model.optimize()

    sugar_intake = model.objVal

    return sugar_intake