import gurobipy as gp
from gurobipy import GRB

def prob_52(dine_in_place, food_truck):
    """
    Args:
        dine_in_place: an integer, representing the number of dine-in places
        food_truck: an integer, representing the number of food trucks
    Returns:
        obj: an integer, representing the objective value (total number of stores)
    """
    model = gp.Model("sandwich_stores")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="dine_in_places")
    y = model.addVar(vtype=GRB.INTEGER, name="food_trucks")

    # Constraints
    model.addConstr(100*x + 50*y >= 500)
    model.addConstr(8*x + 3*y <= 35)

    # Objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj