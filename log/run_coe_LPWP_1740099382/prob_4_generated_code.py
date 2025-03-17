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
    x = model.addVar(lb=0, ub=150, vtype=GRB.INTEGER, name="desk_lamps")
    y = model.addVar(lb=0, ub=180, vtype=GRB.INTEGER, name="night_lamps")

    # Set objective function
    model.setObjective(5*x + 8*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x >= 30, name="demand_desk_lamps")
    model.addConstr(y >= 50, name="demand_night_lamps")
    model.addConstr(x + y >= 100, name="contract_constraint")

    # Optimize the model
    model.optimize()

    # Get the maximum profit
    obj = model.objVal

    return obj