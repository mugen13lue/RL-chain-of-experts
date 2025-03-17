import gurobipy as gp
from gurobipy import GRB

def prob_208(health_supplement_A, health_supplement_B):
    """
    Args:
        health_supplement_A: an integer, representing the servings of health supplement A
        health_supplement_B: an integer, representing the servings of health supplement B
    Returns:
        obj: an integer, representing the objective value (minimized cost)
    """
    model = gp.Model("health_supplements")

    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")  # servings of health supplement A
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="y")  # servings of health supplement B

    # Constraints
    model.addConstr(30*x + 60*y >= 400, "calcium_constraint")
    model.addConstr(50*x + 10*y >= 50, "magnesium_constraint")

    # Objective function
    model.setObjective(14*x + 25*y, GRB.MINIMIZE)

    # Optimize the model
    model.optimize()

    # Get the minimized cost
    obj = model.objVal

    return obj