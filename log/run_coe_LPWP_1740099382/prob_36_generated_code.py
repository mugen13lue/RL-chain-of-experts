import gurobipy as gp
from gurobipy import GRB

def prob_36(Oil_Max, Oil_Max_Pro, Constraint_A, Constraint_B, Constraint_C):
    """
    Args:
        Oil_Max: an integer, number of containers of Oil Max
        Oil_Max_Pro: an integer, number of containers of Oil Max Pro
        Constraint_A: an integer, value of constraint A
        Constraint_B: an integer, value of constraint B
        Constraint_C: an integer, value of constraint C

    Returns:
        Profit: an integer, maximum profit
    """
    # Create a new model
    model = gp.Model("profit_maximization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="Oil_Max")
    y = model.addVar(vtype=GRB.INTEGER, name="Oil_Max_Pro")

    # Set objective function
    model.setObjective(10*x + 15*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(46*x + 13*y <= Constraint_A, "constraint_A")
    model.addConstr(43*x + 4*y <= Constraint_B, "constraint_B")
    model.addConstr(56*x + 45*y <= Constraint_C, "constraint_C")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj