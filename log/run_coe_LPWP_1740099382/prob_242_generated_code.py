import gurobipy as gp
from gurobipy import GRB

def prob_242(salmon, eggs):
    """
    Args:
        salmon: an integer, the number of bowls of salmon to eat
        eggs: an integer, the number of bowls of eggs to eat
    Returns:
        obj: a float, the objective value (sodium intake)
    """
    model = gp.Model("diet_problem")

    # Variables
    x = model.addVar(name="salmon")
    y = model.addVar(name="eggs")

    # Constraints
    model.addConstr(300*x + 200*y >= 2000, "Calories")
    model.addConstr(15*x + 8*y >= 90, "Protein")
    model.addConstr(80*x + 20*y <= 3000, "Sodium")  # Revised constraint based on problem statement
    model.addConstr(y <= 0.4*x, "MaxEggLimit")

    # Objective
    model.setObjective(80*x + 20*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Return objective value
    return model.objVal