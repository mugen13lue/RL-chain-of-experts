from gurobipy import *

def optimize_animal_delivery(camels, horses):
    """
    Args:
        camels: an integer indicating the number of camels
        horses: an integer indicating the number of horses
    Returns:
        obj: an integer, the minimal number of animals
    """
    m = Model("animal_delivery")

    # Variables
    x = m.addVar(vtype=GRB.INTEGER, name="camels")
    y = m.addVar(vtype=GRB.INTEGER, name="horses")

    # Constraints
    m.addConstr(50*x + 60*y >= 1000, "packages_constraint")
    m.addConstr(20*x + 30*y <= 450, "food_constraint")
    m.addConstr(y <= x, "horse_camel_constraint")

    # Objective
    m.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    return int(m.objVal)