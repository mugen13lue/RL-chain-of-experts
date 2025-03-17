import gurobipy as gp
from gurobipy import GRB

def prob_133(daytime_pills, nighttime_pills, total_painkiller_units, daytime_painkiller_units, daytime_sleep_units, nighttime_painkiller_units, nighttime_sleep_units, min_nighttime_pills, min_daytime_ratio):
    """
    Args:
        daytime_pills: an integer, number of daytime pills
        nighttime_pills: an integer, number of nighttime pills
        total_painkiller_units: an integer, total number of painkiller units
        daytime_painkiller_units: an integer, number of painkiller units in daytime pill
        daytime_sleep_units: an integer, number of sleep units in daytime pill
        nighttime_painkiller_units: an integer, number of painkiller units in nighttime pill
        nighttime_sleep_units: an integer, number of sleep units in nighttime pill
        min_nighttime_pills: an integer, minimum number of nighttime pills
        min_daytime_ratio: a float, minimum ratio of daytime pills compared to total pills

    Returns:
        obj: an integer, objective value (amount of sleep medicine)
    """
    model = gp.Model("painkiller_optimization")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="daytime_pills")
    y = model.addVar(vtype=GRB.INTEGER, name="nighttime_pills")

    # Constraints
    model.addConstr(daytime_painkiller_units*x + nighttime_painkiller_units*y <= total_painkiller_units, "Painkiller")
    model.addConstr(daytime_sleep_units*x + nighttime_sleep_units*y <= GRB.INFINITY, "SleepMedicine")
    model.addConstr(x >= min_daytime_ratio*(x+y), "DaytimePercentage")
    model.addConstr(y >= min_nighttime_pills, "NighttimeMinimum")

    # Objective
    model.setObjective(daytime_sleep_units*x + nighttime_sleep_units*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Return objective value
    return model.objVal