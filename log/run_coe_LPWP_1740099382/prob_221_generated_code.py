import gurobipy as gp
from gurobipy import GRB

def prob_221(personal_license, commercial_license):
    """
    Args:
        personal_license: an integer, representing the number of personal licenses
        commercial_license: an integer, representing the number of commercial licenses
    Returns:
        objective_value: an integer, representing the maximum profit
    """
    # Create a new model
    model = gp.Model("license_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="personal_license")
    y = model.addVar(vtype=GRB.INTEGER, name="commercial_license")

    # Set objective function
    model.setObjective(450*x + 1200*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x + y <= 300, "production_limit")
    model.addConstr(550*x + 2000*y <= 400000, "cost_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    objective_value = model.objVal

    return int(objective_value)