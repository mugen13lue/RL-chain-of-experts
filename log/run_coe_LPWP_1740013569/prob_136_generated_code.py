import gurobipy as gp
from gurobipy import GRB

def prob_136(lab_1, lab_2, constraint1, constraint2, constraint3):
    """
    Args:
        lab_1: an integer representing the number of hours to run lab 1
        lab_2: an integer representing the number of hours to run lab 2
        constraint1: an integer representing the available worker hours
        constraint2: an integer representing the minimum number of heart medication pills
        constraint3: an integer representing the minimum number of lung medication pills
    Returns:
        obj: an integer representing the total time needed
    """
    model = gp.Model("pharmaceutical_production")

    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")  # Hours lab 1 is run
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y")  # Hours lab 2 is run

    # Constraints
    model.addConstr(3*x + 5*y <= constraint1, "worker_hours_constraint")
    model.addConstr(20*x + 30*y >= constraint2, "heart_medication_constraint")
    model.addConstr(30*x + 40*y >= constraint3, "lung_medication_constraint")

    # Objective
    model.setObjective(3*x + 5*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Get total time needed
    obj = model.objVal

    return obj