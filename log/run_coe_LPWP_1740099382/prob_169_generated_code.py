import gurobipy as gp
from gurobipy import GRB

def prob_169(camels, horses):
    """
    Args:
        camels: an integer indicating the number of camels
        horses: an integer indicating the number of horses
    Returns:
        obj: an integer, the minimal number of animals
    """
    m = gp.Model("animal_delivery")

    # Variables
    x = m.addVar(vtype=GRB.INTEGER, name="camels")
    y = m.addVar(vtype=GRB.INTEGER, name="horses")

    # Constraints
    m.addConstr(50*x + 60*y >= 1000, "packages")
    m.addConstr(20*x + 30*y <= 450, "food")
    m.addConstr(y <= x, "horses")

    # Objective
    m.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    # Return optimal objective value
    return int(m.objVal)