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
    # Create a new model
    model = gp.Model("smoothie_shop")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="acai_berry_smoothies")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="banana_chocolate_smoothies")

    # Set objective function: minimize total amount of water used
    model.setObjective(3*x + 4*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(7*x + 3*y <= 3500, "acai_berry_constraint")
    model.addConstr(6*x + 4*y <= 3200, "banana_chocolate_constraint")
    model.addConstr(x >= 0.35*(x+y), "at_least_35_percent_acai_berry")
    model.addConstr(y >= x, "more_banana_chocolate_than_acai_berry")

    # Optimize the model
    model.optimize()

    # Get the total amount of water used
    amount_of_water = model.objVal

    return amount_of_water