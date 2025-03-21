import gurobipy as gp
from gurobipy import GRB

def prob_270(smoothie, protein_bar):
    """
    Args:
        smoothie (int): Number of smoothies.
        protein_bar (int): Number of protein bars.

    Returns:
        obj (int): Objective value (maximum protein intake).
    """
    # Create a new model
    model = gp.Model("diet_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="smoothies")
    y = model.addVar(vtype=GRB.INTEGER, name="protein_bars")

    # Set objective function
    model.setObjective(2*x + 7*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(2*x + 7*y <= smoothie*2 + protein_bar*7, "protein_intake_limit")
    model.addConstr(300*x + 250*y <= 2000, "calorie_intake_limit")
    model.addConstr(y == 2*x, "protein_bar_smoothie_ratio")

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj