import gurobipy as gp
from gurobipy import GRB

def prob_275(chemical_A, chemical_B):
    """
    Args:
        chemical_A: an integer representing the amount of chemical A
        chemical_B: an integer representing the amount of chemical B
    Returns:
        obj: an integer representing the total time
    """
    t_A = 30
    t_B = 45
    max_ratio = 1/3
    min_A = 300
    min_total = 1500

    # Create a new model
    model = gp.Model("chemical_mixer")

    # Define decision variables
    A = model.addVar(lb=min_A, vtype=GRB.CONTINUOUS, name="A")
    B = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="B")

    # Set objective function
    model.setObjective(t_A * A + t_B * B, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(A + B >= min_total, "min_total_constraint")
    model.addConstr(A <= max_ratio * B, "max_ratio_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj