import gurobipy as gp
from gurobipy import GRB

def prob_4(desk_lamps, night_lamps):
    """
    Args:
        desk_lamps: an integer, representing the number of desk lamps to be made
        night_lamps: an integer, representing the number of night lamps to be made
    Returns:
        obj: an integer, representing the maximum profit
    """
    # Create a new model
    model = gp.Model("lamp_production")

    # Define decision variables
    x = model.addVar(lb=30, ub=150, vtype=GRB.INTEGER, name="desk_lamps")
    y = model.addVar(lb=50, ub=180, vtype=GRB.INTEGER, name="night_lamps")

    # Set objective function
    model.setObjective(5*x + 8*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x + y >= 100, "min_total_lamps")
    
    # Optimize model
    model.optimize()

    # Get the maximum profit
    obj = model.objVal

    return obj