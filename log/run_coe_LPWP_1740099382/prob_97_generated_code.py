import gurobipy as gp
from gurobipy import GRB

def prob_97(premium_model, regular_model):
    """
    Args:
        premium_model: an integer, number of premium printers
        regular_model: an integer, number of regular printers
    Returns:
        objective_value: an integer, total number of printers
    """
    # Create a new model
    model = gp.Model("printer_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="premium_printers")
    y = model.addVar(vtype=GRB.INTEGER, name="regular_printers")

    # Set objective function: minimize total number of printers
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(30*x + 20*y >= 200, "pages_per_minute")
    model.addConstr(4*x + 3*y <= 35, "ink_per_minute")
    model.addConstr(y <= x, "num_regular_printers")

    # Optimize the model
    model.optimize()

    # Get the total number of printers
    objective_value = model.objVal

    return int(objective_value)