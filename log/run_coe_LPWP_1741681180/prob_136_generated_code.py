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
    x1 = model.addVar(vtype=GRB.CONTINUOUS, name="lab_1_hours")
    x2 = model.addVar(vtype=GRB.CONTINUOUS, name="lab_2_hours")

    # Objective function: minimize total time needed
    model.setObjective(3*x1 + 5*x2, GRB.MINIMIZE)

    # Constraints
    model.addConstr(20*x1 + 30*x2 >= constraint2, "heart_medication_constraint")
    model.addConstr(30*x1 + 40*x2 >= constraint3, "lung_medication_constraint")
    model.addConstr(3*x1 + 5*x2 <= constraint1, "worker_hours_constraint")

    # Optimize model
    model.optimize()

    # Get total time needed
    obj = model.objVal

    return obj