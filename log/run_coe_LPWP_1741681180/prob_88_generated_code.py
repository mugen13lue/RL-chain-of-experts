import gurobipy as gp
from gurobipy import GRB

def prob_88(glass, plastic, glass_capacity, plastic_capacity, glass_min, glass_to_plastic_ratio, available_water):
    """
    Args:
        glass: an integer, representing the number of glass bottles
        plastic: an integer, representing the number of plastic bottles
        glass_capacity: an integer, representing the capacity of a glass bottle in ml
        plastic_capacity: an integer, representing the capacity of a plastic bottle in ml
        glass_min: an integer, representing the minimum number of glass bottles
        glass_to_plastic_ratio: an integer, representing the ratio of plastic bottles to glass bottles
        available_water: an integer, representing the available water in ml

    Returns:
        obj: an integer, representing the maximum number of bottles
    """
    model = gp.Model("water_bottles")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="glass_bottles", lb=glass_min)
    y = model.addVar(vtype=GRB.INTEGER, name="plastic_bottles", lb=glass_to_plastic_ratio * glass_min)

    # Objective function: maximize total number of bottles
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(glass_capacity * x + plastic_capacity * y <= available_water, "water_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj