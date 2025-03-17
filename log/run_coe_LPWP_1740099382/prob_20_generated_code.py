import gurobipy as gp
from gurobipy import GRB

def prob_20(banana_haters_package, combo_package):
    """
    Args:
        banana_haters_package: an integer representing the quantity of banana-haters packages
        combo_package: an integer representing the quantity of combo packages
    Returns:
        obj: an integer representing the maximum net profit
    """
    # Create a new model
    model = gp.Model("profit_maximization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="banana_haters_packages")
    y = model.addVar(vtype=GRB.INTEGER, name="combo_packages")

    # Set objective function
    model.setObjective(6*x + 7*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(6*x + 5*y <= 10, "apples_constraint")
    model.addConstr(6*y <= 20, "bananas_constraint")
    model.addConstr(30*x + 20*y <= 80, "grapes_constraint")

    # Optimize the model
    model.optimize()

    # Get the maximum net profit
    obj = model.objVal

    return obj