from gurobipy import *

def prob_283(full_time_staff, part_time_staff):
    """
    Args:
        full_time_staff: an integer, representing the number of full-time staff
        part_time_staff: an integer, representing the number of part-time staff
    Returns:
        obj: an integer, representing the objective value
    """
    # Create a new model
    model = Model("staff_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="full_time_staff")
    y = model.addVar(vtype=GRB.INTEGER, name="part_time_staff")

    # Set objective: minimize the total number of staff hired
    model.setObjective(x + y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(40*x + 15*y >= 1000, "total_hours_constraint")
    model.addConstr(1280*x + 450*y <= 31500, "budget_constraint")

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj