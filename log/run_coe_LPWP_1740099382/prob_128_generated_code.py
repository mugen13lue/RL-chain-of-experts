import gurobipy as gp
from gurobipy import GRB

def prob_128(liquid_hand_sanitizer, foam_hand_sanitizer, water, alcohol, available_water, available_alcohol, liquid_constraint, foam_constraint):
    """
    Args:
        liquid_hand_sanitizer: an integer, the number of liquid hand sanitizers made
        foam_hand_sanitizer: an integer, the number of foam hand sanitizers made
        water: an integer, the amount of water required for each hand sanitizer
        alcohol: an integer, the amount of alcohol required for each hand sanitizer
        available_water: an integer, the available amount of water
        available_alcohol: an integer, the available amount of alcohol
        liquid_constraint: an integer, the maximum number of liquid hand sanitizers that can be made
        foam_constraint: an integer, the maximum number of foam hand sanitizers that can be made

    Returns:
        obj: an integer, the maximum number of hands that can be cleaned
    """
    model = gp.Model("hand_sanitizer")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="liquid_hand_sanitizer")
    y = model.addVar(vtype=GRB.INTEGER, name="foam_hand_sanitizer")

    # Constraints
    model.addConstr(40*x + 60*y <= 2000, "water_constraint")
    model.addConstr(50*x + 40*y <= 2100, "alcohol_constraint")
    model.addConstr(x <= liquid_constraint, "liquid_constraint")
    model.addConstr(y >= x, "foam_constraint")

    # Objective
    model.setObjective(30*x + 20*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)