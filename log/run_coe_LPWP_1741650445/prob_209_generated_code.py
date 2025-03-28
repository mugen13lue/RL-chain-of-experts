import gurobipy as gp
from gurobipy import GRB

def prob_209():
    """
    Returns:
        obj: an integer representing the minimum cost
    """
    model = gp.Model("dog_food_mixing")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="regular_bags")
    y = model.addVar(vtype=GRB.INTEGER, name="premium_bags")

    # Constraints
    model.addConstr(4*x + 12*y >= 15)
    model.addConstr(7*x + 10*y >= 20)
    model.addConstr(10*x + 16*y >= 20)

    # Objective
    model.setObjective(20*x + 35*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    obj = model.objVal

    return obj