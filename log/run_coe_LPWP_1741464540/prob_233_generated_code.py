import gurobipy as gp
from gurobipy import GRB

def prob_233(high_volume, low_volume):
    """
    Args:
        high_volume: an integer, number of high-volume pipes
        low_volume: an integer, number of low-volume pipes
    Returns:
        obj: an integer, objective value
    """
    # Create a new model
    model = gp.Model("pipe_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of high-volume pipes
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of low-volume pipes

    # Set objective function: minimize total number of pipes
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(10000*x + 5000*y >= 150000, "Demand_Constraint")
    model.addConstr(12*x + 5*y <= 160, "Technician_Constraint")
    model.addConstr(x <= 0.35*(x+y), "High-Volume_Pipe_Limit")
    model.addConstr(y >= 8, "Low-Volume_Pipe_Minimum")
    model.addConstr(y <= 0.65*(x+y), "Low-Volume_Pipe_Limit")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj