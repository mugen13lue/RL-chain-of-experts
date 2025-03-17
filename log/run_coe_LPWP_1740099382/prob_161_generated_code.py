import gurobipy as gp
from gurobipy import GRB

def prob_161(new_one, old_one, new_one_, old_one_):
    """
    Args:
        new_one: an integer, number of gifts delivered per trip by the new company
        old_one: an integer, number of gifts delivered per trip by the old company
        new_one_: an integer, liters of diesel used per trip by the new company
        old_one_: an integer, liters of diesel used per trip by the old company

    Returns:
        total_amount_of_diesel: an integer, total amount of diesel used
    """
    # Create a new model
    model = gp.Model("gift_delivery")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of trips made by the new company
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of trips made by the old company

    # Set objective function: minimize total diesel usage
    model.setObjective(new_one_ * x + old_one_ * y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(new_one * x + old_one * y >= 1000, "gifts_constraint")
    model.addConstr(new_one_ * x <= 30 * 15, "diesel_constraint_new")
    model.addConstr(old_one * y >= 0.4 * (x + y), "diesel_constraint_old")

    # Optimize the model
    model.optimize()

    # Get the total amount of diesel used
    total_amount_of_diesel = model.objVal

    return total_amount_of_diesel