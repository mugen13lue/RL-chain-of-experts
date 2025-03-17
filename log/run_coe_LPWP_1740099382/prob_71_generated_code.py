import gurobipy as gp
from gurobipy import GRB

def prob_71(top_loading_model, front_loading_model, var1, var2, var3, var4):
    """
    Args:
        top_loading_model: an integer, representing the number of top-loading machines
        front_loading_model: an integer, representing the number of front-loading machines
        var1: an integer, representing the number of items the top-loading model can wash per day
        var2: an integer, representing the number of items the front-loading model can wash per day
        var3: an integer, representing the amount of energy consumed by the top-loading model per day
        var4: an integer, representing the amount of energy consumed by the front-loading model per day
    Returns:
        x: an integer, representing the optimal number of top-loading machines
        y: an integer, representing the optimal number of front-loading machines
    """
    m = gp.Model("laundromat")

    # Define variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")  # number of top-loading machines
    y = m.addVar(vtype=GRB.INTEGER, name="y")  # number of front-loading machines

    # Set objective
    m.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    m.addConstr(var1*x + var2*y >= 5000, "Items_Constraint")
    m.addConstr(var3*x + var4*y <= 7000, "Energy_Constraint")
    m.addConstr(x <= 0.4*(x+y), "Top-loading_Limit")
    m.addConstr(y >= 10, "Front-loading_Minimum")

    # Optimize model
    m.optimize()

    # Get the optimal number of top-loading and front-loading machines
    x_optimal = round(x.x)
    y_optimal = round(y.x)

    return x_optimal, y_optimal