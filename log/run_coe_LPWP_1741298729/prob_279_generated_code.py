import gurobipy as gp
from gurobipy import GRB

def prob_279(matcha_ice_cream, orange_sorbet):
    """
    Args:
        matcha_ice_cream: an integer representing the number of matcha ice cream desserts
        orange_sorbet: an integer representing the number of orange sorbet desserts
    Returns:
        obj: an integer representing the total amount of flavouring needed
    """
    model = gp.Model("dessert_shop")

    # Variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="matcha_ice_cream")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="orange_sorbet")

    # Constraints
    model.addConstr(2*x + 4*y <= 600, "flavouring")
    model.addConstr(3*y <= 550, "water")
    model.addConstr(x >= 0.15*(x+y), "minimum_matcha_ice_cream")

    # Objective
    model.setObjective(4*x + 4*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)