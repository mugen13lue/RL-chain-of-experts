import gurobipy as gp
from gurobipy import GRB

def prob_182(helicopter, car):
    """
    Solves the Fish Transportation Problem and calculates the total time needed.

    Args:
        helicopter: an integer representing the number of helicopter trips
        car: an integer representing the number of car trips

    Returns:
        obj: an integer representing the total time needed
    """
    model = gp.Model("Fish_Transportation")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of helicopter trips
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of car trips

    # Constraints
    model.addConstr(x >= 0)
    model.addConstr(y >= 0)
    model.addConstr(30*x + 20*y >= 300)
    model.addConstr(x <= 5)
    model.addConstr(y >= 0.6*(x + y))

    # Objective
    model.setObjective(40*x + 30*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Get total time needed
    obj = model.objVal

    return obj