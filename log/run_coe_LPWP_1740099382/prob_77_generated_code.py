import gurobipy as gp
from gurobipy import GRB

def prob_77(dual, single):
    """
    Args:
        dual: an integer, representing the number of dual model stamping machines
        single: an integer, representing the number of single model stamping machines
    Returns:
        obj: an integer, representing the total number of stamping machines
    """
    
    # Create a new model
    model = gp.Model("stamp_machines")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="dual_machines")
    y = model.addVar(vtype=GRB.INTEGER, name="single_machines")

    # Set objective function: minimize total number of stamping machines
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(50*x + 30*y >= 300, "stamping_rate")
    model.addConstr(20*x + 15*y <= 135, "glue_usage")
    model.addConstr(y >= x, "quietness_constraint")

    # Optimize model
    model.optimize()

    # Get the total number of stamping machines
    obj = model.objVal

    return obj