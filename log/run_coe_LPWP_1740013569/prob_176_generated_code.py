import gurobipy as gp
from gurobipy import GRB

def prob_176(small, large):
    """
    Args:
        small: an integer, number of small jars
        large: an integer, number of large jars
    Returns:
        obj: an integer, the objective value
    """
    S = 50  # capacity of small jar in ml
    L = 200  # capacity of large jar in ml
    C = 100000  # minimum amount of jam to be shipped

    # Create a new model
    model = gp.Model("jam_shipping")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of small jars
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of large jars

    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(S * x + L * y >= C, "min_jam_requirement")
    model.addConstr(y <= x, "large_small_jars")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj