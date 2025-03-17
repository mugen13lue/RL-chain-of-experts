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
    potassium = model.addVar(vtype=GRB.INTEGER, name="potassium")

    # Set objective function: maximize potassium intake
    model.setObjective(potassium, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(15*salads + 3*fruit_bowls >= 90, "Vitamin")
    model.addConstr(7*salads + 12*fruit_bowls >= 110, "Fibre")
    model.addConstr(2*salads + 8*fruit_bowls == potassium, "Potassium")
    model.addConstr(fruit_bowls <= 0.3*(salads + fruit_bowls), "Fruit_Bowl_Percentage")

    # Optimize the model
    model.optimize()

    # Get the maximum potassium intake
    objective_value = model.objVal

    return int(objective_value)