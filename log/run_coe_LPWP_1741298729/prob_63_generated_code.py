import gurobipy as gp
from gurobipy import GRB

def prob_63(counter_top_sized, fridge_sized_one):
    """
    Args:
        counter_top_sized: an integer, representing the number of counter-top sized machines
        fridge_sized_one: an integer, representing the number of fridge sized machines

    Returns:
        obj: an integer, representing the objective value (number of machines)
    """
    model = gp.Model("ice_cream_machine")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="counter_top")
    y = model.addVar(vtype=GRB.INTEGER, name="fridge")

    # Constraints
    model.addConstr(50*x + 70*y <= 500)
    model.addConstr(80*x + 150*y >= 1000)

    # Objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)