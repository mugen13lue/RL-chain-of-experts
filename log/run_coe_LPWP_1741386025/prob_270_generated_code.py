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
    obj = -1 * (2 * smoothie + 7 * protein_bar)  # Objective function to maximize protein intake

    # Create a new model
    model = gp.Model("diet_optimization")

    # Create variables
    x = model.addVar(vtype=GRB.INTEGER, name="smoothies")
    y = model.addVar(vtype=GRB.INTEGER, name="protein_bars")

    # Set objective
    model.setObjective(2 * x + 7 * y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(2 * x + 7 * y <= 2 * smoothie + 7 * protein_bar, "protein_limit")
    model.addConstr(300 * x + 250 * y <= 2000, "calories_limit")
    model.addConstr(y >= 2 * x, "protein_bar_constraint")

    # Optimize model
    model.optimize()

    if model.status == GRB.OPTIMAL:
        obj = model.objVal
    else:
        obj = -1

    return obj