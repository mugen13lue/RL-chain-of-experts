import gurobipy as gp
from gurobipy import GRB

def prob_96(milk_chocolate_bars, dark_chocolate_bars):
    """
    Args:
        milk_chocolate_bars: an integer, representing the number of milk chocolate bars
        dark_chocolate_bars: an integer, representing the number of dark chocolate bars
    Returns:
        total_production_time: an integer, representing the total production time
    """
    model = gp.Model("chocolate_production")

    # Variables
    milk_bars = model.addVar(vtype=GRB.INTEGER, name="milk_chocolate_bars")
    dark_bars = model.addVar(vtype=GRB.INTEGER, name="dark_chocolate_bars")

    # Constraints
    model.addConstr(4*milk_bars + 6*dark_bars <= 2000, "cocoa_constraint")
    model.addConstr(7*milk_bars + 3*dark_bars <= 1750, "milk_constraint")
    model.addConstr(milk_bars >= 2*dark_bars, "milk_dark_ratio_constraint")

    # Objective
    model.setObjective(15*milk_bars + 12*dark_bars, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    total_production_time = model.objVal

    return total_production_time