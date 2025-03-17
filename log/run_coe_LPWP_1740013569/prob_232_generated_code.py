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
    model = gp.Model("science_fair")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="circular_tables")
    y = model.addVar(vtype=GRB.INTEGER, name="rectangular_tables")

    # Constraints
    model.addConstr(4*x + 4*y <= 500, "participants_constraint")
    model.addConstr(4*x + 5*y <= 300, "poster_boards_constraint")
    model.addConstr(15*x + 20*y <= 1900, "space_constraint")

    # Objective
    model.setObjective(8*x + 12*y, GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)