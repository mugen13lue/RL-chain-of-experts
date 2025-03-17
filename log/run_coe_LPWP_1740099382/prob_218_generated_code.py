import gurobipy as gp
from gurobipy import GRB

def prob_218():
    """
    Returns:
        obj: an integer, the maximum profit
    """
    # Create a new model
    model = gp.Model("taco_stand")

    # Define decision variables
    x1 = model.addVar(lb=0, ub=50, vtype=GRB.INTEGER, name="regular_tacos")
    x2 = model.addVar(lb=0, ub=40, vtype=GRB.INTEGER, name="deluxe_tacos")

    # Set objective function
    model.setObjective(2.50*x1 + 3.55*x2, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x1 + x2 <= 70, "total_tacos")
    
    # Optimize model
    model.optimize()

    # Get the maximum profit
    obj = model.objVal

    return obj