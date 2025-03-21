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
    # Create a new model
    model = gp.Model("plant_nutrition")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")  # kg of fertilizer A
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y")  # kg of fertilizer B
    D = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="D")  # amount of vitamin D

    # Set objective function: minimize amount of vitamin D
    model.setObjective(D, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(13*x + 8*y >= 220, "Nitrogen")
    model.addConstr(5*x + 14*y >= 160, "Phosphoric Acid")
    model.addConstr(6*x + 6*y <= 350, "Vitamin A")
    model.addConstr(5*x + 9*y == D, "Vitamin D")

    # Optimize model
    model.optimize()

    # Get the optimal solution
    obj = model.objVal

    return obj