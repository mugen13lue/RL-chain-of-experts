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

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of helicopter trips
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of car trips

    # Constraints
    model.addConstr(30*x + 20*y >= 300, "Fish_constraint")
    model.addConstr(x <= 5, "Helicopter_trips_constraint")
    model.addConstr(y >= 0.6*(x+y), "Car_trips_constraint")

    # Objective
    model.setObjective(40*x + 30*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Retrieve the total time needed
    obj = model.objVal

    return obj