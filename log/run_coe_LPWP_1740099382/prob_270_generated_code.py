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
    smoothies = model.addVar(vtype=GRB.INTEGER, name="smoothies")
    protein_bars = model.addVar(vtype=GRB.INTEGER, name="protein_bars")

    # Set objective function
    model.setObjective(2*smoothies + 7*protein_bars, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(2*smoothies + 7*protein_bars <= 2*protein_bar, "protein_constraint")
    model.addConstr(300*smoothies + 250*protein_bars <= 2000, "calories_constraint")
    model.addConstr(protein_bars >= 2*smoothies, "protein_bar_constraint")

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj