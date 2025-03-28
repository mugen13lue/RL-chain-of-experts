import gurobipy as gp
from gurobipy import GRB

def prob_184(medium, large, _2, _30, _4, _70, three, _60, _5):
    """
    Args:
        medium: an integer, the number of medium sized carts
        large: an integer, the number of large sized carts
        _2: an integer, horse requirement for medium sized cart
        _30: an integer, rice carrying capacity of medium sized cart
        _4: an integer, horse requirement for large sized cart
        _70: an integer, rice carrying capacity of large sized cart
        three: an integer, ratio of medium to large sized carts
        _60: an integer, available horses
        _5: an integer, minimum number of medium and large sized carts
    Returns:
        amount_of_rice: an integer, maximum amount of rice that can be transported
    """
    model = gp.Model("rice_transportation")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="medium_carts")
    y = model.addVar(vtype=GRB.INTEGER, name="large_carts")

    # Objective function: maximize the amount of rice transported
    model.setObjective(30*x + 70*y, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(2*x + 4*y <= 60, "horse_constraint")
    model.addConstr(x >= 3*y, "ratio_constraint")
    model.addConstr(x >= 5, "min_medium_constraint")
    model.addConstr(y >= 5, "min_large_constraint")

    model.optimize()

    amount_of_rice = model.objVal

    return amount_of_rice