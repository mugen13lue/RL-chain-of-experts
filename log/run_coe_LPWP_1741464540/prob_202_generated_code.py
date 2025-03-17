import gurobipy as gp
from gurobipy import GRB

def prob_202(desks, drawers, assembly_constraint, sanding_constraint):
    """
    Args:
        desks: an integer, representing the number of desks
        drawers: an integer, representing the number of drawers
        assembly_constraint: an integer, representing the available minutes for assembly
        sanding_constraint: an integer, representing the available minutes for sanding
    Returns:
        profit: an integer, representing the maximum profit
    """
    # Create a new model
    model = gp.Model("profit_maximization")

    # Create decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="desks")
    y = model.addVar(vtype=GRB.INTEGER, name="drawers")

    # Set objective function
    model.setObjective(100*x + 90*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(40*x + 30*y <= assembly_constraint, "assembly_constraint")
    model.addConstr(20*x + 10*y <= sanding_constraint, "sanding_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal solution
    profit = model.objVal

    return profit