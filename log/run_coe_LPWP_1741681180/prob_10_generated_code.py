import gurobipy as gp
from gurobipy import GRB

def prob_10(A, B, constraint1, constraint2, constraint3):
    """
    Args:
        A: an integer, kg of fertilizer A
        B: an integer, kg of fertilizer B
        constraint1: an integer, constraint 1 value
        constraint2: an integer, constraint 2 value
        constraint3: an integer, constraint 3 value
    Returns:
        obj: an integer, amount of vitamin D
    """
    model = gp.Model("plant_nutrition")

    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")  # kg of fertilizer A
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="y")  # kg of fertilizer B

    # Objective function: minimize the amount of vitamin D
    model.setObjective(5*x + 9*y, sense=GRB.MINIMIZE)

    # Constraints
    model.addConstr(13*x + 8*y >= constraint1)  # nitrogen constraint
    model.addConstr(5*x + 14*y >= constraint2)  # phosphoric acid constraint
    model.addConstr(6*x + 6*y <= constraint3)  # vitamin A constraint

    # Optimize the model
    model.optimize()

    # Get the optimal solution
    obj = model.objVal

    return obj