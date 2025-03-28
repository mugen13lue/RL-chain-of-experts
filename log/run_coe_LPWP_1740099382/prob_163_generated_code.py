import gurobipy as gp
from gurobipy import GRB

def prob_163(helicopters, trucks):
    """
    Args:
        helicopters: an integer, the number of helicopters
        trucks: an integer, the number of trucks
    Returns:
        obj: an integer, the amount of pollution
    """
    # Create a new model
    m = gp.Model("transportation")

    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")  # number of helicopter trips
    y = m.addVar(vtype=GRB.INTEGER, name="y")  # number of truck trips

    # Set objective function
    m.setObjective(5*x + 10*y, GRB.MINIMIZE)

    # Add constraints
    m.addConstr(3*x + 7*y >= 80, "cows_constraint")
    m.addConstr(y <= 8, "truck_trips_constraint")
    m.addConstr(x >= 0, "non_negativity_x")
    m.addConstr(y >= 0, "non_negativity_y")

    # Optimize model
    m.optimize()

    # Get the optimal objective value
    obj = m.objVal

    return obj