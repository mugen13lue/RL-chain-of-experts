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

    # Variables
    x = model.addVar(lb=0, ub=Max_Bikes, vtype=GRB.INTEGER, name="bikes")
    y = model.addVar(lb=Min_Scooters, vtype=GRB.INTEGER, name="scooters")

    # Objective Function
    model.setObjective(8*x + 5*y, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(3*x + 2*y <= Charge_Limit, "charge_constraint")
    model.addConstr(x <= 0.3*(x + y), "bike_limit")
    model.addConstr(y >= Min_Scooters, "scooter_limit")

    # Optimize the model
    model.optimize()

    return int(model.objVal)