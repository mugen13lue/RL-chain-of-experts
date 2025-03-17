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
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of densely-seated ski lifts
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of loosely-seated ski lifts

    # Set objective function: Minimize Z = x + y
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(45*x + 20*y >= 1000)
    model.addConstr(30*x + 22*y <= 940)
    model.addConstr(y >= 5)

    # Optimize the model
    model.optimize()

    # Get the total number of ski lifts needed
    total_lifts = int(x.x + y.x)

    return total_lifts