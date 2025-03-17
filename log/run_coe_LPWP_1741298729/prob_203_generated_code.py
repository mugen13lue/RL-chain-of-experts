import gurobipy as gp
from gurobipy import GRB

def prob_203():
    """
    Returns:
        obj: a float, the maximum profit
    """
    # Create a new model
    model = gp.Model("milk_tea_production")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="black_milk_tea")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="matcha_milk_tea")

    # Set objective function
    model.setObjective(7.5*x + 5*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(600*x + 525*y <= 30000, "milk_constraint")
    model.addConstr(10*x + 5*y <= 500, "honey_constraint")

    # Optimize model
    model.optimize()

    # Get the maximum profit
    obj = model.objVal

    return obj