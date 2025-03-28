import gurobipy as gp
from gurobipy import GRB

def prob_107(fish, chicken):
    """
    Args:
        fish: an integer, number of fish meals
        chicken: an integer, number of chicken meals
    Returns:
        obj: an integer, minimized fat intake
    """
    model = gp.Model("minimize_fat_intake")

    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="fish_meals")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="chicken_meals")
    F = model.addVar(lb=0, vtype=GRB.INTEGER, name="total_fat_intake")

    # Constraints
    model.addConstr(10*x + 15*y >= 130)
    model.addConstr(12*x + 8*y >= 120)
    model.addConstr(7*x + 10*y == F)

    # Objective
    model.setObjective(F, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    obj = model.objVal

    return obj