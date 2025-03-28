import gurobipy as gp
from gurobipy import GRB

def prob_135(sulfate, ginger, constraint1, constraint2, constraint3):
    """
    Args:
        sulfate: an integer, the amount of sulfate to be added to the shampoo.
        ginger: an integer, the amount of ginger to be added to the shampoo.
        constraint1: a float, the amount of time it takes for one unit of sulfate to be effective.
        constraint2: a float, the amount of time it takes for one unit of ginger to be effective.
        constraint3: a string, the constraint on the ratio of sulfate to ginger.
    Returns:
        obj: the total amount of time it takes for the mixture to be effective.
    """
    # Create a new model
    model = gp.Model("shampoo_optimization")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="sulfate", obj=0.5)
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="ginger", obj=0.75)

    # Set objective function
    model.setObjective(0.5*x + 0.75*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(x >= 100, name="sulfate_constraint")
    model.addConstr(x + y <= 400, name="total_ingredient_constraint")
    model.addConstr(x <= 2*y, name="sulfate_to_ginger_ratio_constraint")

    # Optimize the model
    model.optimize()

    # Get the total amount of time it takes for the mixture to be effective
    obj = model.objVal

    return obj