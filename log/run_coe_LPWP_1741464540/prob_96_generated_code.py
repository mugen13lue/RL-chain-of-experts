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
    x = model.addVar(vtype=GRB.INTEGER, name="milk_chocolate_bars")
    y = model.addVar(vtype=GRB.INTEGER, name="dark_chocolate_bars")

    # Constraints
    model.addConstr(4*x + 6*y <= 2000, "cocoa_constraint")
    model.addConstr(7*x + 3*y <= 1750, "milk_constraint")
    model.addConstr(x >= 2*y, "milk_chocolate_ratio_constraint")

    # Objective
    model.setObjective(15*x + 12*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    total_production_time = model.objVal

    return total_production_time