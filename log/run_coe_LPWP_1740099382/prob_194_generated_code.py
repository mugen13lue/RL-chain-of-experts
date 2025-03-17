import gurobipy as gp
from gurobipy import GRB

def prob_194(small_trucks, large_trucks):
    """
    Args:
        small_trucks: an integer, representing the number of small trucks
        large_trucks: an integer, representing the number of large trucks
    Returns:
        obj: an integer, representing the maximum amount of snow that can be transported
    """
    model = gp.Model("snow_removal")

    # Define variables
    x = model.addVar(vtype=GRB.INTEGER, name="small_trucks")
    y = model.addVar(vtype=GRB.INTEGER, name="large_trucks")

    # Set objective function
    model.setObjective(30*x + 50*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(2*x + 4*y <= 30, "people_constraint")
    model.addConstr(x >= 10, "small_trucks_constraint")
    model.addConstr(y >= 3, "large_trucks_constraint")
    model.addConstr(x == 2*y, "ratio_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj