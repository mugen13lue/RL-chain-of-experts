import gurobipy as gp
from gurobipy import GRB

def prob_266(acai_berry_smoothie, banana_chocolate_smoothie):
    """
    Args:
        acai_berry_smoothie: an integer, represents the number of acai berry smoothies
        banana_chocolate_smoothie: an integer, represents the number of banana chocolate smoothies
    Returns:
        amount_of_water: an integer, total amount of water used
    """
    model = gp.Model("smoothie_shop")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="acai_berry_smoothies", obj=3)
    y = model.addVar(vtype=GRB.INTEGER, name="banana_chocolate_smoothies", obj=4)

    # Constraints
    model.addConstr(7*x <= 3500, "acai_berry_units")
    model.addConstr(6*y <= 3200, "banana_chocolate_units")
    model.addConstr(x >= 0.35*(x+y), "minimum_acai_berry_percentage")
    model.addConstr(y >= x, "banana_chocolate_must_be_more")

    # Objective
    model.setObjective(3*x + 4*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    amount_of_water = model.objVal

    return amount_of_water