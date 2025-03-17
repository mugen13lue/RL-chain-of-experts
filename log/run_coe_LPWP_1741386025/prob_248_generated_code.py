from gurobipy import *

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
    model = Model("navy_ship_nutrition")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="salad")
    y = model.addVar(vtype=GRB.INTEGER, name="fruit_bowl")

    # Set objective: Maximize K = 2x + 8y
    model.setObjective(2 * x + 8 * y, GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(7 * x + 15 * y >= 90, "Vitamin")
    model.addConstr(12 * x + 3 * y >= 110, "Fibre")
    model.addConstr(2 * x + 8 * y == x + y, "Potassium")
    model.addConstr(y <= 0.3 * (x + y), "Fruit_Bowl_Limit")

    # Optimize the model
    model.optimize()

    # Get the maximum potassium intake
    objective_value = model.objVal

    return int(objective_value)