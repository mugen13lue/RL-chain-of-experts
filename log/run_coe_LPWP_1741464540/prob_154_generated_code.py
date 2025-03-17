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
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of small teams
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of large teams

    # Set objective function
    model.setObjective(50*x + 80*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(3*x + 5*y <= 150, "employees_constraint")
    model.addConstr(x >= 10, "small_teams_constraint")
    model.addConstr(y >= 6, "large_teams_constraint")
    model.addConstr(x >= 3*y, "small_to_large_teams_ratio_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = int(model.objVal)

    return obj