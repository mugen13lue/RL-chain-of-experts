import gurobipy as gp
from gurobipy import GRB

def prob_165(electric_bikes, scooters, Max_Bikes, Min_Scooters, Charge_Limit):
    """
    Args:
        electric_bikes: an integer, the number of electric bikes used.
        scooters: an integer, the number of scooters used.
        Max_Bikes: an integer, maximum number of electric bikes allowed.
        Min_Scooters: an integer, minimum number of scooters required.
        Charge_Limit: an integer, available charge units.

    Returns:
        Number_of_Meals: an integer, the maximum number of meals that can be delivered.
    """
    model = gp.Model("meal_delivery")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="electric_bikes")
    y = model.addVar(vtype=GRB.INTEGER, name="scooters")

    # Objective function: maximize the number of meals delivered
    model.setObjective(8*x + 5*y, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(3*x + 2*y <= Charge_Limit, "charge_limit")
    model.addConstr(x <= Max_Bikes, "max_bikes")
    model.addConstr(y >= Min_Scooters, "min_scooters")
    model.addConstr(x <= 0.3*(x + y), "max_bikes_percentage")

    # Optimize the model
    model.optimize()

    # Return the maximum number of meals that can be delivered
    return int(model.objVal)