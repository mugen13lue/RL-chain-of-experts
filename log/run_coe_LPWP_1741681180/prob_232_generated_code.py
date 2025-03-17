import gurobipy as gp
from gurobipy import GRB

def prob_232(circular_tables, rectangular_tables):
    """
    Args:
        circular_tables: an integer, the number of circular tables
        rectangular_tables: an integer, the number of rectangular tables
    Returns:
        objective: an integer, the maximum number of catered guests
    """
    # Create a new model
    model = gp.Model("science_fair")

    # Define the decision variables
    circular_guests = model.addVar(vtype=GRB.INTEGER, name="circular_guests")
    rectangular_guests = model.addVar(vtype=GRB.INTEGER, name="rectangular_guests")

    # Set objective function: maximize the total number of catered guests
    model.setObjective(circular_guests + rectangular_guests, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(5 * 4 * circular_tables * circular_guests + 4 * 4 * rectangular_tables * rectangular_guests >= 500, "participants_constraint")
    model.addConstr(4 * 4 * circular_tables + 4 * 12 * rectangular_tables <= 300, "poster_boards_constraint")
    model.addConstr(15 * circular_tables + 20 * rectangular_tables <= 1900, "space_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    objective = int(model.objVal)

    return objective