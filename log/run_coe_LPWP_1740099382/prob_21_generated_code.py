import gurobipy as gp
from gurobipy import GRB

def prob_21():
    """
    This function solves the given problem to maximize total profit.

    Returns:
        obj: The maximum total profit.
    """
    # Create a new model
    model = gp.Model("bakery_problem")

    # Define decision variables
    x = model.addVar(vtype=GRB.CONTINUOUS, name="bread")
    y = model.addVar(vtype=GRB.CONTINUOUS, name="cookies")

    # Set objective function
    model.setObjective(5*x + 3*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x + 0.5*y <= 3000, "machine_hours_constraint")
    model.addConstr(3*x + y <= 3000, "oven_hours_constraint")
    model.addConstr(x >= 0, "non_negativity_bread")
    model.addConstr(y >= 0, "non_negativity_cookies")

    # Optimize the model
    model.optimize()

    # Get the maximum total profit
    obj = model.objVal

    return obj