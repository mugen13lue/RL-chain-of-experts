from gurobipy import *

def prob_96(milk_chocolate_bars, dark_chocolate_bars):
    """
    Args:
        milk_chocolate_bars: an integer, representing the number of milk chocolate bars
        dark_chocolate_bars: an integer, representing the number of dark chocolate bars
    Returns:
        total_production_time: an integer, representing the total production time
    """
    m = Model()

    # Variables
    milk_choco_bars = m.addVar(vtype=GRB.INTEGER, name="milk_chocolate_bars")
    dark_choco_bars = m.addVar(vtype=GRB.INTEGER, name="dark_chocolate_bars")

    # Constraints
    m.addConstr(4*milk_choco_bars + 6*dark_choco_bars <= 2000)
    m.addConstr(7*milk_choco_bars + 3*dark_choco_bars <= 1750)
    m.addConstr(milk_choco_bars >= 2*dark_choco_bars)
    m.addConstr(milk_choco_bars >= 0)
    m.addConstr(dark_choco_bars >= 0)

    # Objective
    m.setObjective(15*milk_choco_bars + 12*dark_choco_bars, GRB.MINIMIZE)

    m.optimize()

    total_production_time = m.objVal

    return total_production_time