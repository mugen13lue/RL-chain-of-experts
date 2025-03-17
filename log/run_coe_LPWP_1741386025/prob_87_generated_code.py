import gurobipy as gp
from gurobipy import GRB

def prob_87(manual_slicers, automatic_slicers, constraint1, constraint2, constraint3):
    """
    Args:
        manual_slicers: an integer, represents the number of manual slicers
        automatic_slicers: an integer, represents the number of automatic slicers
        constraint1: a string, represents the constraint "manual_slicers <= automatic_slicers"
        constraint2: a string, represents the constraint "5 * manual_slicers + 8 * automatic_slicers >= 50"
        constraint3: a string, represents the constraint "3 * manual_slicers + 6 * automatic_slicers <= 35"
    Returns:
        obj: an integer, represents the minimum total number of slicers
    """
    # Create a new model
    model = gp.Model("slicer_problem")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="manual_slicers")
    y = model.addVar(vtype=GRB.INTEGER, name="automatic_slicers")

    # Set objective function: minimize total number of slicers based on efficiency
    model.setObjective(5 * x + 8 * y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(x <= y, name="manual_less_than_automatic")
    model.addConstr(5 * x + 8 * y >= 50, name="slices_per_minute_constraint")
    model.addConstr(3 * x + 6 * y <= 35, name="grease_per_minute_constraint")

    # Optimize the model
    model.optimize()

    # Return the optimal objective value
    return int(model.objVal)  # Convert to integer for output consistency