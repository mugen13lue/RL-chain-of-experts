import gurobipy as gp
from gurobipy import GRB

def prob_117(burgers, pizza):
    """
    Args:
        burgers: an integer, the number of burgers
        pizza: an integer, the number of pizza slices
    Returns:
        obj: an integer, the objective value (cholesterol intake)
    """
    model = gp.Model("cholesterol_intake")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="burgers")
    y = model.addVar(vtype=GRB.INTEGER, name="pizza_slices")

    # Constraints
    model.addConstr(10*x + 8*y >= 130, "fat_constraint")
    model.addConstr(300*x + 250*y >= 3000, "calories_constraint")
    model.addConstr(y >= 2*x, "pizza_burger_ratio")
    model.addConstr(12*x + 10*y <= GRB.INFINITY, "cholesterol_constraint")

    # Objective
    model.setObjective(12*x + 10*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)