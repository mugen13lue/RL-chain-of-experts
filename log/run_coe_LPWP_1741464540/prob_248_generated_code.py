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
    salads = model.addVar(vtype=GRB.INTEGER, name="salads")
    fruit_bowls = model.addVar(vtype=GRB.INTEGER, name="fruit_bowls")

    # Set objective function
    model.setObjective(2*salads + 8*fruit_bowls, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(7*salads + 15*fruit_bowls >= 90, "Vitamin")
    model.addConstr(12*salads + 3*fruit_bowls >= 110, "Fibre")
    model.addConstr(0.3*(salads + fruit_bowls) >= fruit_bowls, "Fruit_Bowl_Percentage")

    # Optimize model
    model.optimize()

    # Get the maximum potassium intake
    objective_value = model.objVal

    return objective_value