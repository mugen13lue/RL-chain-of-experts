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
    x = model.addVar(vtype=GRB.INTEGER, name="acai_berry_smoothies")
    y = model.addVar(vtype=GRB.INTEGER, name="banana_chocolate_smoothies")

    # Constraints
    model.addConstr(7*x + 3*y <= 3500, "acai_berries_constraint")
    model.addConstr(6*x + 4*y <= 3200, "banana_chocolate_constraint")
    model.addConstr(x >= 0, "non_negativity_constraint_acai")
    model.addConstr(y >= 0, "non_negativity_constraint_banana")
    model.addConstr(x >= 0.35*(x + y), "at_least_35_percent_constraint")
    model.addConstr(y >= x, "banana_chocolate_popularity_constraint")

    # Objective
    model.setObjective(3*x + 4*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    amount_of_water = model.objVal

    return amount_of_water