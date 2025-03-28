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

    # Parameters
    S_d = 100
    S_f = 50
    E_d = 8
    E_f = 3
    R = 500
    E_total = 35

    # Objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Constraints
    model.addConstr(S_d * x >= R)
    model.addConstr(S_f * y >= R)
    model.addConstr(E_d * x + E_f * y <= E_total)

    # Optimize model
    model.optimize()

    obj = model.objVal

    return obj