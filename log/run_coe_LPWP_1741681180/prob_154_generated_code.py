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
    small_team_count = model.addVar(vtype=GRB.INTEGER, name="small_teams")
    large_team_count = model.addVar(vtype=GRB.INTEGER, name="large_teams")

    # Set objective function: maximize the amount of lawn mowed
    model.setObjective(50 * small_team_count + 80 * large_team_count, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(3 * small_team_count >= large_team_count)  # Number of small teams must be at least 3 times the number of large teams
    model.addConstr(small_team_count >= 10)  # At least 10 small teams
    model.addConstr(large_team_count >= 6)  # At least 6 large teams
    model.addConstr(3 * small_team_count + 5 * large_team_count <= 150)  # Total number of employees available

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = int(model.objVal)

    return obj