import gurobipy as gp
from gurobipy import GRB

def prob_161(gifts_per_trip_new, gifts_per_trip_old, diesel_per_trip_new, diesel_per_trip_old):
    """
    Args:
        gifts_per_trip_new: an integer, number of gifts delivered per trip by the new company
        gifts_per_trip_old: an integer, number of gifts delivered per trip by the old company
        diesel_per_trip_new: an integer, liters of diesel used per trip by the new company
        diesel_per_trip_old: an integer, liters of diesel used per trip by the old company

    Returns:
        total_amount_of_diesel: an integer, total amount of diesel used
    """
    # Create a new model
    model = gp.Model("gift_delivery")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of trips made by the new company
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of trips made by the old company

    # Set objective function
    model.setObjective(diesel_per_trip_new * x + diesel_per_trip_old * y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(gifts_per_trip_new * x + gifts_per_trip_old * y >= 1000, "gifts_constraint")
    model.addConstr(diesel_per_trip_new * x <= 30 * 15, "diesel_constraint_new")
    model.addConstr(diesel_per_trip_old * y >= 0.4 * (x + y), "diesel_constraint_old")

    # Optimize the model
    model.optimize()

    # Get the total amount of diesel used
    total_amount_of_diesel = model.objVal

    return total_amount_of_diesel