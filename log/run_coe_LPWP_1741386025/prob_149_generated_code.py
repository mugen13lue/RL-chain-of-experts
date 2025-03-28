import gurobipy as gp
from gurobipy import GRB

def prob_149(vans, trucks):
    """
    Args:
        vans: an integer, the number of trips by vans
        trucks: an integer, the number of trips by trucks
    Returns:
        obj: an integer, the objective value
    """
    m = gp.Model("transportation")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")  # number of trips by vans
    y = m.addVar(vtype=GRB.INTEGER, name="y")  # number of trips by trucks

    # Constraints
    m.addConstr(50*x + 80*y >= 1500, "transportation_constraint")
    m.addConstr(30*x + 50*y <= 1000, "budget_constraint")
    m.addConstr(x >= y, "van_trips_more_than_truck_trips")

    # Objective
    m.setObjective(30*x + 50*y, GRB.MINIMIZE)  # Minimize the total cost of transportation

    # Optimize model
    m.optimize()

    # Return objective value
    return m.objVal