import gurobipy as gp
from gurobipy import GRB

def prob_167(small_wagons, large_wagons, twice):
    """
    Args:
        small_wagons: an integer, number of small wagons
        large_wagons: an integer, number of large wagons
        twice: an integer, twice the number of large wagons
    Returns:
        obj: an integer, number of wagons
    """
    model = gp.Model("wagon_optimization")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(x >= 2*y)
    model.addConstr(y >= 10)
    model.addConstr(20*x + 50*y == 2000)

    # Objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    obj = model.objVal

    return obj