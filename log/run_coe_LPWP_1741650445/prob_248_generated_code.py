import gurobipy as gp
from gurobipy import GRB

def prob_248(salad, fruit_bowl):
    """
    Find the maximum potassium intake for a navy ship's staff.

    Args:
        salad: An integer representing the number of salads prepared.
        fruit_bowl: An integer representing the number of fruit bowls prepared.

    Returns:
        objective_value: An integer representing the maximum potassium intake.
    """
    # Create a new model
    model = gp.Model("navy_ship_nutrition")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="salad")
    y = model.addVar(vtype=GRB.INTEGER, name="fruit_bowl")

    # Set objective function
    model.setObjective(2*x + 8*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(15*x + 3*y >= 90, "vitamin")
    model.addConstr(12*x + 3*y >= 110, "fibre")
    model.addConstr(y <= 0.3*(x + y), "proportion")

    # Optimize model
    model.optimize()

    # Get the maximum potassium intake
    objective_value = model.objVal

    return objective_value