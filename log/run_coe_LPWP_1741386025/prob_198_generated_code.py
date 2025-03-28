import gurobipy as gp
from gurobipy import GRB

def prob_198(vans, cars):
    """
    Solve the voter transportation problem.

    Args:
        vans: an integer, number of vans
        cars: an integer, number of cars

    Returns:
        obj: an integer, total number of cars used
    """
    obj = 1e9

    # Create a new model
    m = gp.Model("voter_transportation")

    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="vans")
    y = m.addVar(vtype=GRB.INTEGER, name="cars")

    # Set objective
    m.setObjective(y, GRB.MINIMIZE)

    # Add constraints
    m.addConstr(6*x + 3*y >= 200, "transporting_voters")
    m.addConstr(x <= 0.3*(x + y), "limit_on_vans")

    # Optimize model
    m.optimize()

    if m.status == GRB.OPTIMAL:
        obj = int(m.objVal)

    return obj