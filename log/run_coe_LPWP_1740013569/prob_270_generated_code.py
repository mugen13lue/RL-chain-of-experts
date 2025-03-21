from gurobipy import *

def prob_270(smoothie, protein_bar):
    """
    Args:
        smoothie (int): Number of smoothies.
        protein_bar (int): Number of protein bars.

    Returns:
        obj (int): Objective value (maximum protein intake).
    """
    # Create a new model
    model = Model("diet_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="smoothie")
    y = model.addVar(vtype=GRB.INTEGER, name="protein_bar")

    # Set objective: Maximize 2x + 7y
    model.setObjective(2 * x + 7 * y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(2 * x + 7 * y <= 2000, "protein_constraint")
    model.addConstr(300 * x + 250 * y <= 2000, "calories_constraint")
    model.addConstr(y >= 2 * x, "protein_bar_requirement")

    # Optimize the model
    model.optimize()

    # Return the objective value
    return int(model.objVal)