from gurobipy import *

def prob_194(small_trucks, large_trucks):
    """
    Args:
        small_trucks: an integer, representing the number of small trucks
        large_trucks: an integer, representing the number of large trucks
    Returns:
        obj: an integer, representing the maximum amount of snow that can be transported
    """
    m = Model()

    # Define variables
    x = m.addVar(vtype=GRB.INTEGER, name="small_trucks")
    y = m.addVar(vtype=GRB.INTEGER, name="large_trucks")

    # Set objective
    m.setObjective(30*x + 50*y, sense=GRB.MAXIMIZE)

    # Add constraints
    m.addConstr(2*x + 4*y <= 30, "total_people")
    m.addConstr(x >= 10, "min_small_trucks")
    m.addConstr(y >= 3, "min_large_trucks")
    m.addConstr(x == 2*y, "small_large_ratio")

    # Optimize model
    m.optimize()

    obj = int(m.objVal)

    return obj