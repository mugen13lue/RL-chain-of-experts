from gurobipy import *

def prob_286(wine, kombucha, fruit_per_wine, water_per_wine, fruit_per_kombucha, tea_per_kombucha, total_water, total_tea, percent_kombucha):
    """
    Args:
        wine: an integer representing the number of wine units
        kombucha: an integer representing the number of kombucha units
        fruit_per_wine: an integer representing the units of fruit required for wine
        water_per_wine: an integer representing the units of water required for wine
        fruit_per_kombucha: an integer representing the units of fruit required for kombucha
        tea_per_kombucha: an integer representing the units of tea required for kombucha
        total_water: an integer representing the total units of water available
        total_tea: an integer representing the total units of tea available
        percent_kombucha: an integer representing the percentage of kombucha products

    Returns:
        obj: an integer representing the objective value
    """
    m = Model("brewery")

    # Decision variables
    wine_units = m.addVar(vtype=GRB.INTEGER, name="wine_units")
    kombucha_units = m.addVar(vtype=GRB.INTEGER, name="kombucha_units")

    # Objective function
    m.setObjective(fruit_per_wine * wine_units + fruit_per_kombucha * kombucha_units, GRB.MINIMIZE)

    # Constraints
    m.addConstr(water_per_wine * wine_units + tea_per_kombucha * kombucha_units <= total_water, "water_constraint")
    m.addConstr(tea_per_kombucha * kombucha_units <= total_tea, "tea_constraint")
    m.addConstr(wine_units >= kombucha_units, "wine_larger_than_kombucha")
    m.addConstr(kombucha_units / (wine_units + kombucha_units) >= percent_kombucha / 100, "kombucha_percentage")

    m.optimize()

    if m.status == GRB.OPTIMAL:
        obj = m.objVal
    else:
        obj = 1e9

    return obj