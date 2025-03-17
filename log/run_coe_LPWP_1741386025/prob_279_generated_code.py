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

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="matcha_ice_cream")
    y = model.addVar(vtype=GRB.INTEGER, name="orange_sorbet")

    # Constraints
    model.addConstr(2*x + 4*y <= 600, "ice_cream_constraint")
    model.addConstr(3*y <= 550, "water_constraint")
    model.addConstr(0.15*(x + y) <= x, "matcha_percentage_constraint")

    # Objective function
    model.setObjective(2*x + 4*y, GRB.MINIMIZE)

    # Optimize the model
    model.optimize()

    if model.status == GRB.OPTIMAL:
        return int(model.objVal)
    else:
        return 1e9  # Return a large number if no optimal solution found