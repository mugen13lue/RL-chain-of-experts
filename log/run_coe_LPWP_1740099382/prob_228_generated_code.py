import gurobipy as gp
from gurobipy import GRB

def prob_228(densely_seated_one, loosely_seated_one):
    """
    Solve the ski lifts problem to minimize the total number of ski lifts needed.

    Args:
        densely_seated_one: Number of densely-seated ski lifts (integer).
        loosely_seated_one: Number of loosely-seated ski lifts (integer).

    Returns:
        total_lifts: Total number of ski lifts needed (integer).
    """
    # Create a new model
    model = gp.Model("ski_lifts")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="densely_seated_lifts")
    y = model.addVar(vtype=GRB.INTEGER, name="loosely_seated_lifts")

    # Set objective function: minimize total number of ski lifts
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(30*x + 22*y <= 940, "electricity_constraint")
    model.addConstr(45*x + 20*y >= 1000, "guests_constraint")
    model.addConstr(y >= 5, "min_loosely_seated_constraint")

    # Optimize the model
    model.optimize()

    # Get the total number of ski lifts needed
    total_lifts = model.objVal

    return total_lifts