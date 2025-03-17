import gurobipy as gp
from gurobipy import GRB

def prob_158():
    """
    Returns:
        objective_value: an integer, the total number of buses
    """
    model = gp.Model("bus_hiring")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(20*x + 50*y >= 500, "Transportation_Capacity")
    model.addConstr(y <= 0.2*(x + y), "Maximum_Large_Buses")
    model.addConstr(x >= 0, "Non-negativity_x")
    model.addConstr(y >= 0, "Non-negativity_y")

    # Objective
    model.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Get objective value
    objective_value = model.objVal

    return objective_value