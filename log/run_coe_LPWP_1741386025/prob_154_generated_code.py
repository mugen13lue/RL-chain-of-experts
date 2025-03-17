import gurobipy as gp
from gurobipy import GRB

def prob_154(small_teams, large_teams):
    """
    Args:
        small_teams: an integer
        large_teams: an integer
    Returns:
        obj: an integer, the amount of lawn that can be mowed
    """
    # Create a new model
    model = gp.Model("lawn_mowing")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="small_teams")
    y = model.addVar(vtype=GRB.INTEGER, name="large_teams")

    # Set objective function
    model.setObjective(50*x + 80*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(3*x + 5*y <= 150, "employees_constraint")
    model.addConstr(x >= 3*y, "small_teams_constraint")
    model.addConstr(y >= 6, "minimum_large_teams_constraint")
    model.addConstr(x >= 10, "minimum_small_teams_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj