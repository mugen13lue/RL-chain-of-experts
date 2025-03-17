import gurobipy as gp
from gurobipy import GRB

def prob_158(small_buses, large_buses):
    """
    Args:
        small_buses: an integer, number of small buses to hire
        large_buses: an integer, number of large buses to hire

    Returns:
        objective_value: an integer, the total number of buses
    """
    model = gp.Model("bus_hiring")

    # Decision Variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="small_buses")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="large_buses")

    # Constraints
    model.addConstr(20*x + 50*y >= 500, "Transportation_Capacity")
    model.addConstr(y <= 0.2*(x + y), "Maximum_Large_Buses")

    # Objective Function
    model.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    objective_value = model.objVal

    return int(objective_value)