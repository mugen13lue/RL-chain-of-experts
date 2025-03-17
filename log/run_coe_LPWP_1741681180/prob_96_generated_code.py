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

    # Decision variables
    x1 = model.addVar(vtype=GRB.INTEGER, name="milk_chocolate_bars")
    x2 = model.addVar(vtype=GRB.INTEGER, name="dark_chocolate_bars")

    # Objective function: minimize total production time
    model.setObjective(15*x1 + 12*x2, GRB.MINIMIZE)

    # Constraints
    model.addConstr(4*x1 + 6*x2 <= 2000, "cocoa_constraint")
    model.addConstr(7*x1 + 3*x2 <= 1750, "milk_constraint")
    model.addConstr(x1 >= 2*x2, "milk_dark_ratio_constraint")

    # Optimize model
    model.optimize()

    total_production_time = model.objVal

    return total_production_time