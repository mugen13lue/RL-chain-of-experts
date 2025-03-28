from gurobipy import *

def prob_63(counter_top_sized, fridge_sized_one):
    """
    Args:
        counter_top_sized: an integer, representing the number of counter-top sized machines
        fridge_sized_one: an integer, representing the number of fridge sized machines

    Returns:
        obj: an integer, representing the objective value (number of machines)
    """
    m = Model("ice_cream_machine")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="counter_top")
    y = m.addVar(vtype=GRB.INTEGER, name="fridge")

    # Objective function
    m.setObjective(x + y, GRB.MINIMIZE)

    # Constraints
    m.addConstr(50*x + 70*y <= 500, "heat_output")
    m.addConstr(80*x + 150*y >= 1000, "ice_cream_production")

    # Optimize model
    m.optimize()

    return int(m.objVal)