import gurobipy as gp
from gurobipy import GRB

def prob_245(large_cruise_ship, small_cruise_ship):
    """
    Args:
        large_cruise_ship: an integer, number of large cruise ships used
        small_cruise_ship: an integer, number of small cruise ships used

    Returns:
        amount_of_pollution: an integer, total amount of pollution produced
    """
    # Create a new model
    model = gp.Model("cruise_ship_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of large cruise ship trips
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of small cruise ship trips

    # Set objective function: Minimize 20x + 15y
    model.setObjective(20*x + 15*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(2000*x + 800*y >= 20000, "total_customers_constraint")
    model.addConstr(x <= 7, "total_large_trips_constraint")
    model.addConstr(y >= 0.4*(x+y), "percentage_small_trips_constraint")

    # Optimize model
    model.optimize()

    # Get the total amount of pollution produced
    amount_of_pollution = model.objVal

    return amount_of_pollution